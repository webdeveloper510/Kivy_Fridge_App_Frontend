from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
import json
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivymd.uix.snackbar import Snackbar

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.url = 'http://127.0.0.1:8000/register/'
        self.request = None  

    def register_user(self):
        Firstname = self.ids.first_name.text
        Lastname = self.ids.last_name.text
        phone_number = self.ids.mobile.text
        email = self.ids.email.text
        password = self.ids.password.text

        payload = {
            'Firstname': Firstname,
            'Lastname': Lastname,
            'phone_number':phone_number,
            'email': email,
            'password': password,
        }

        self.request = UrlRequest(
            self.url,
            on_success=self.on_success,
            on_failure=self.on_failure,
            req_body=json.dumps(payload),
            req_headers={'Content-type': 'application/json'}
        )

    def on_success(self, request, result):
        print('User registered successfully!')
        snackbar = Snackbar(
                text="[color=#ddbb34]         You have Register Successfully[/color]",
                snackbar_y="10dp",
                snackbar_x="30dp",
                size_hint_x=.9
            ).open()
        self.manager.current = 'home'

    def on_failure(self, request, result):
        error_message = next(iter(result.values()))[0]
        print(error_message)
        snackbar = Snackbar(
                text="[color=#ddbb34]          "+str(error_message)+"[/color]",
                snackbar_y="10dp",
                snackbar_x="25dp",
                size_hint_x=.9
            ).open()
        self.manager.current = 'register'

    
   
   