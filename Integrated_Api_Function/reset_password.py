from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
import json
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.properties import StringProperty

class ResetPasswordScreen(Screen):
    email = StringProperty('')
    print(email)
    def __init__(self, **kwargs):
        super(ResetPasswordScreen, self).__init__(**kwargs)
        self.url ='http://127.0.0.1:8000/resetpassword/'
        self.request = None  
    
   
    def send_passwordset_request(self):
        password = self.ids.password_field.text
        confirm_password=self.ids.confirm_password_field.text
        email=self.email
        print(email)
        
    
        payload = {
            'email': email,
            'password': password,
            'confirm_password':confirm_password,
        }
        self.request = UrlRequest(
            self.url,
            on_success=self.on_password_reset_success,
            on_failure=self.on_password_reset_failure,
            req_body=json.dumps(payload),
            req_headers={'Content-type': 'application/json'}
        )

    def on_password_reset_success(self, request, result):
        print("result success------>",result)
        dialog = MDDialog(
            title="Success",
            text=result['message'],
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=self.dismiss_success_dialog
                )
            ]
        )
        dialog.open()
    
    def dismiss_success_dialog(self, *args):
        self.manager.current = 'home'

    def on_password_reset_failure(self, request, result):
        print("resultfailure------>",result)
        dialog = MDDialog(
            title="Error",
            text=result['message'],
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=self.dismiss_failure_dialog
                )
            ]
        )
        dialog.open()
    
    def dismiss_failure_dialog(self, *args):
        self.manager.current = 'reset_password'