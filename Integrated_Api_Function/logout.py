from kivy.network.urlrequest import UrlRequest
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

class LogoutManager:
    def __init__(self, access_token):
        self.access_token = None

    def set_access_token(self, access_token):
        self.access_token = access_token


    def logout(self):
        headers = {'Authorization': 'Bearer ' + self.access_token}
        url = "http://127.0.0.1:8000/logout/" 

        req = UrlRequest(
            url,
            method='POST',
            req_headers=headers,
            on_success=self.on_success,
            on_failure=self.on_failure
        )

    def on_success(self, req, result):
        dialog = MDDialog(
            title=result['message'],
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=self.dismiss_success_dialog
                )
            ]
        )
        dialog.open()
    
    def dismiss_success_dialog(self, *args):
        self.manager.current = 'login'
        

    def on_failure(self, req, result):
       
        print("Logout failed")
       