from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
import json
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

class OTPScreen(Screen):

    def __init__(self, **kwargs):
        super(OTPScreen, self).__init__(**kwargs)
        self.url ='http://127.0.0.1:8000/email_otp/'
        self.request = None  
    
    def send_otp_request(self):
        otp = self.ids.otp_field.text
    
        payload = {
            'otp': otp,
        }
        self.request = UrlRequest(
            self.url,
            on_success=self.on_otp_success,
            on_failure=self.on_otp_failure,
            req_body=json.dumps(payload),
            req_headers={'Content-type': 'application/json'}
        )

    def on_otp_success(self, request, result):
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
        self.manager.current = 'reset_password'

    def on_otp_failure(self, request, result):
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
        self.manager.current = 'OTP_Screen'