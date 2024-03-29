from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.network.urlrequest import UrlRequest
import json
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import Snackbar
from Integrated_Api_Function.url import Base_Url

class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.url = '{}/login/'.format(Base_Url)
        self.request = None  
    
    def login(self):
        email = self.ids.email.text
        password = self.ids.password.text
    
        payload = {
            'email': email,
            'password': password,
        }
        self.request = UrlRequest(
            self.url,
            on_success=self.on_login_success,
            on_failure=self.on_login_error,
            req_body=json.dumps(payload),
            req_headers={'Content-type': 'application/json'}
        )

    def on_login_success(self, request, result):
        # print(result['message'])
        access_token = result['token']['access']
        id=result['id']
    
        snackbar = Snackbar(
                text="[color=#ddbb34]                 Login Successfull[/color]",
                snackbar_y="10dp",
                snackbar_x="30dp",
                size_hint_x=.9
            ).open()
        
        self.manager.current = 'home'
        self.manager.get_screen('edit_profile').set_access_token(access_token)
        self.manager.get_screen('settings').set_access_token(access_token)
        self.manager.get_screen('edit_profile').set_id(id)# set user_id 
        self.manager.get_screen('camera').set_id(id)# set id 
        self.manager.get_screen('home').set_id(id)# set user_id  for home screen 
        self.manager.get_screen('expiry_item_screen').set_id(id)# set user_id  for expiry_item_screen
        self.manager.get_screen('green_item_screen').set_id(id)# set user_id  for green_item_screen
        self.manager.get_screen('useby_item_screen').set_id(id)# set user_id  for useby_item_screen


    def on_login_error(self, request, result):

        error_message=result['message']
        snackbar = Snackbar(
                text="[color=#ddbb34]          "+str(error_message)+"[/color]",
                snackbar_y="10dp",
                snackbar_x="25dp",
                size_hint_x=.9
            ).open()
        self.manager.current ='login'
        
