from kivy.clock import Clock
from kivy.graphics.texture import Texture
from PIL import Image as PILImage
import io
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
import cv2
import requests
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.toolbar import MDTopAppBar
from kivy.graphics import Color, Rectangle
from kivy.network.urlrequest import UrlRequest



class MyCamera(Screen):
    def __init__(self, **kwargs):
        super(MyCamera, self).__init__(**kwargs)
        self.url = "http://127.0.0.1:8000/capture_image/"
        self.request = None  

       
        box_layout = BoxLayout(orientation='vertical')
        with box_layout.canvas.before:
            Color(0, 0, 0, 1)  # Black color
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        self.add_widget(box_layout)

        
        top_bar = MDTopAppBar(title='Camera',left_action_items=[["arrow-left", lambda *args: setattr(self.manager, "current", "home")]])
        box_layout.add_widget(top_bar)

        # Add the camera preview image
        self.image = Image()
        box_layout.add_widget(self.image)

        # Create the capture button as an MDRectangleFlatButton
        self.capture_button = MDRectangleFlatButton(
            text="Capture",
            on_release=self.capture_image,
            theme_text_color="Custom",
            md_bg_color=(0, 0.7, 1, 1),
            text_color=(1, 1, 1, 1),  
            pos_hint={'center_x': 0.5},
            size_hint=(None, None),
            width=Window.width * 0.3,  
            height=Window.width * 0.1  
        )

        # Create a BoxLayout for the capture button at the bottom center
        capture_button_layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=Window.height * 0.1)
        spacer = Widget(size_hint=(1, 1))
        capture_button_layout.add_widget(spacer)
        capture_button_layout.add_widget(self.capture_button)
        box_layout.add_widget(capture_button_layout)

        # Create the camera object
        self.camera = cv2.VideoCapture(0)

        self.capture_frame_event = None
        self.capture_frame()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def capture_frame(self, *args):
        ret, frame = self.camera.read()

        if ret:
            buf = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt="bgr"
            )
            texture.blit_buffer(buf, colorfmt="bgr", bufferfmt="ubyte")
            self.image.texture = texture

        self.image.texture_size = self.image.texture.size
        self.capture_frame_event = Clock.schedule_once(
            self.capture_frame, 1 / 30
        )  # Update frame every 1/30 second
    
    def set_id(self, id):
        self.id = id

    def capture_image(self, *args):
        image_path = "captured_image.png"  # Path to save the captured image

        ret, frame = self.camera.read()
        if ret:
            cv2.imwrite(image_path, frame)
            print(f"Image captured and saved to: {image_path}")

            # Convert the image to PNG format
            pil_image = PILImage.open(image_path)
            png_image_stream = io.BytesIO()
            pil_image.save(png_image_stream, format='PNG')
            png_image_stream.seek(0)

            url = self.url
            payload = {
                'user_id': str(self.id),
            }

            files = {
                'image': ('image.png', png_image_stream, 'image/png')
            }

            response = requests.post(url, data=payload, files=files)
            print(response.json())

            if response.status_code == 200:
                print("Image uploaded successfully.")
            else:
                print("Failed to send request.")
            
    # def on_success(self, req, result):
    #  print(result)
            
    # print("Image uploaded successfully.")
    
    # def on_failure(self, req, result):      
    #  print(result)  

    #  print("Failed to send request.")