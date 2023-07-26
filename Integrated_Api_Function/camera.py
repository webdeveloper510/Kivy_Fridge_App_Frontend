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
from kivy.uix.modalview import ModalView
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.utils import get_color_from_hex
from Integrated_Api_Function.url import Base_Url



class MyCamera(Screen):
    def __init__(self, **kwargs):
        super(MyCamera, self).__init__(**kwargs)
        self.url = "{}/capture_image/".format(Base_Url)
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
        image_path = "captured_image.png"  

        ret, frame = self.camera.read()
        if ret:
            cv2.imwrite(image_path, frame)
            # print(f"Image captured and saved to: {image_path}")

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
            response_data=(response.json())
            
            
            item_name_array=[]
            item_id_array=[]
            for item_data in response_data['data']:
                item_id = item_data['id']
                item_name = item_data['item']
                created_at = item_data['created_at']
                last_updated = item_data['last_updated']
                item_id_array.append(item_id)
                item_name_array.append(item_name)

            if response.status_code == 200:
                self.show_dialog(response_data)
                self.manager.get_screen('expiry_screen').set_itemlist(item_name_array)
                self.manager.get_screen('expiry_screen').set_itemid(item_id_array)
                
            else:
                print("Failed to send request.")
    
    def show_dialog(self, data):
        items = data['data']
        item_names = [item['item'] for item in items]
        item_text = '\n'.join(item_names)

        self.dialog = MDDialog(
            title="Would you like to add these items in fridge",
            text=item_text,
            radius=[20, 7, 20, 7],
            buttons=[
                MDFlatButton(
                    text="No",
                    on_release=self.dismiss_dialog
                ),
                MDFlatButton(
                    text="Yes",
                    on_release=self.proceed_to_screen1
                )
            ]
        )
        self.dialog.open()

    def dismiss_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()

    def proceed_to_screen1(self, *args):
        self.dismiss_dialog()
        self.manager.current = 'expiry_screen'

            
   