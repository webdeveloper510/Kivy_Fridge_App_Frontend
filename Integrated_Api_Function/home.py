from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import  Screen
from kivy.network.urlrequest import UrlRequest
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.button import MDFlatButton
import requests
from Integrated_Api_Function.url import Base_Url
import json
from kivy.app import App

        
class AsyncImageButton(ButtonBehavior, AsyncImage):
    def __init__(self, image_url, food_item_id,user_id, **kwargs):
        super(AsyncImageButton, self).__init__(**kwargs)
        self.source = image_url
        self.size_hint = (0.8, 0.8)
        self.food_item_id = food_item_id
        self.user_id=user_id
        self.id = None
        self.bind(on_release=self.on_image_click)



    def on_image_click(self, *args):
        dialog = MDDialog(
            title="Would you like to remove this item from the fridge?",
            radius=[20, 7, 20, 7],
            buttons=[
                MDFlatButton(
                    text="Yes",
                    on_release=self.remove_item_from_fridge
                ),
                MDFlatButton(
                    text="No",
                    on_release=lambda *x: dialog.dismiss()
                )
            ]
        )
       
        dialog.open()
        dialog.bind(on_dismiss=self.on_dialog_dismiss)

    def on_dialog_dismiss(self, *args):
        app = App.get_running_app()
        if args[0].text == 'Yes':
            app.root.current = 'home' 

    def remove_item_from_fridge(self, *args):
     
       
        payload = {
            "user_id":self.user_id,
            "food_item_id": self.food_item_id
        }
    
        headers = {
            'Content-Type': 'application/json'
        }
        url = f'{Base_Url}/delete_fridge_item/'
        UrlRequest(
            url,
            req_headers=headers,
            req_body=json.dumps(payload),
            on_success=self.on_remove_success,
            on_failure=self.on_remove_failure,
            method='POST'
        )

    def on_remove_success(self, req, result):
        print("success result--->",result)
        # pass

    def on_remove_failure(self, req, result):
        print("failure result--->",result)
       
        # pass
   

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.url = None
        self.request = None
        self.id = None

    def set_id(self, id):
        self.id = id
        self.url = '{}/food_itemslist/{}/'.format(Base_Url, self.id)

    def get_user_items(self):
        headers = {
            'Content-Type': 'application/json'
        }
        UrlRequest(
            self.url,
            on_success=self.on_success,
            on_failure=self.on_failure,
            req_headers=headers,
            method='GET'
        )

    def on_success(self, req, result):
        # print("home result", result)
        box_2 = self.ids.box_2
        box_3 = self.ids.box_3
        box_4 = self.ids.box_4
        box_5 = self.ids.box_5
        box_6 = self.ids.box_6
        box_7 = self.ids.box_7
        box_8 = self.ids.box_8
        box_9 = self.ids.box_9
        box_10 = self.ids.box_10
        box_11 = self.ids.box_11
        box_12_child_layout1 = self.ids.box_12_child_layout1
        box_12_child_layout2 = self.ids.box_12_child_layout2
        box_13_child_layout1 = self.ids.box_13_child_layout1
        box_13_child_layout2 = self.ids.box_13_child_layout2

        box_2.clear_widgets()
        box_3.clear_widgets()
        box_4.clear_widgets()
        box_5.clear_widgets()
        box_6.clear_widgets()
        box_7.clear_widgets()
        box_8.clear_widgets()
        box_9.clear_widgets()
        box_10.clear_widgets()
        box_11.clear_widgets()
        box_13_child_layout1.clear_widgets()
        box_13_child_layout2.clear_widgets()

        for items in result['data']:
            image_url = items['image_url']
            category = items['category']
            food_item_id = items['id']
            user_id=items['user_id']
            async_image = AsyncImageButton(image_url,food_item_id,user_id)
            
            if category == 'Dairy':
                box_2.add_widget(async_image)

            elif category == 'Meat':
                box_3.add_widget(async_image)

            elif category == 'Veg': 
                box_4.add_widget(async_image)
            
            elif category == 'Fruit': 
                box_5.add_widget(async_image)

            elif category == 'Sauces': 
                box_9.add_widget(async_image)

            elif category == 'Grain Group': 
                box_10.add_widget(async_image)

            elif category == 'Cooked Foods':
                box_11.add_widget(async_image)

            elif category == 'Egg':
                box_13_child_layout1.add_widget(async_image)

            elif category == 'Frozen Dessert': 
                box_13_child_layout2.add_widget(async_image)
            

    def on_enter(self):
        self.get_user_items()

    def on_failure(self, req, result):
        # print("failure", result)
        pass




