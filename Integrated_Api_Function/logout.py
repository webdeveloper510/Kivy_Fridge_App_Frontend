from kivy.network.urlrequest import UrlRequest
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from Integrated_Api_Function.url import Base_Url
from kivy.uix.screenmanager import Screen, ScreenManager

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.access_token = None

    def set_access_token(self, access_token):
        self.access_token = access_token
       
    def logout_user(self):
        headers = {'Authorization':'Bearer ' + self.access_token}
        
        url = "{}/logout/".format(Base_Url) 
      

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
        dialog = MDDialog(
            title="Unable to Logout. Please Try again later",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=self.dismiss_success_dialog
                )
            ]
        )
        dialog.open()

        self.manager.current = 'settings'
       