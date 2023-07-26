from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.network.urlrequest import UrlRequest
import json
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from Integrated_Api_Function.url import Base_Url

'{}/update_food_item/'.format(Base_Url),

class ForgetPasswordScreen(Screen):

    def __init__(self, **kwargs):
        super(ForgetPasswordScreen, self).__init__(**kwargs)
        self.url ='{}/resetpasswordemail/'.format(Base_Url)
        self.request = None  
        
    
    def send_reset_password_request(self):
        email = self.ids.email_field.text
    
        payload = {
            'email': email,
        }
        self.request = UrlRequest(
            self.url,
            on_success=self.on_reset_password_success,
            on_failure=self.on_reset_password_failure,
            req_body=json.dumps(payload),
            req_headers={'Content-type': 'application/json'}
        )

    def on_reset_password_success(self, request, result):
        print("result success------>",result)
        email=result['email']
        print("email---->",email)
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
        email = self.ids.email_field.text
        self.manager.current = 'OTP_Screen'
        self.manager.get_screen('reset_password').set_email(email)


    def on_reset_password_failure(self, request, result):
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
        self.manager.current = 'forget_password'