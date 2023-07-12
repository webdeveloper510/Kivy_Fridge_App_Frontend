from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.url = 'http://127.0.0.1:8000/food_itemslist/1/'
        self.request = None

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
        api_response = result

        box_2 =self.ids.box_2
        box_3 =self.ids.box_3
        box_4= self.ids.box_4
        box_5=self.ids.box_5
        box_6=self.ids.box_6
        box_7=self.ids.box_7
        box_8=self.ids.box_8
        box_9=self.ids.box_9
        box_10=self.ids.box_10
        box_11=self.ids.box_11
        box_13_child_layout1= self.ids.box_13_child_layout1
        box_13_child_layout2=self.ids.box_13_child_layout2
        
        for  items in result['data']:
            image_url = items['image_url']
            category = items['category']
            async_image = AsyncImage(source=image_url)
            async_image.size_hint = (0.5, 0.7)
          
            if category == 'Dairy':
              
                box_2.add_widget(async_image)
                     
            if category == 'Meat':
                box_3.add_widget(async_image)
            
            if category =='Sauces': 
                box_9.add_widget(async_image)

            if category =='Grain Group': 
                box_10.add_widget(async_image)

            if category =='Cooked Foods':
                box_11.add_widget(async_image)

            if category == 'Egg':
                box_13_child_layout1.add_widget(async_image)

            if category =='Frozen Dessert': 
                box_13_child_layout2.add_widget(async_image)
            
    def on_enter(self):
        self.get_user_items()

    def on_failure(self, req, result):
        print("failure", result)