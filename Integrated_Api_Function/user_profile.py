import json
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from Integrated_Api_Function.url import Base_Url

class EditProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(EditProfileScreen, self).__init__(**kwargs)
        self.edit_url = '{}/editprofile/'.format(Base_Url)
        self.profile_url = '{}/userprofile/'.format(Base_Url)
        self.request = None
        self.access_token = None
        self.id = None 

    def set_access_token(self, access_token):
        self.access_token = access_token

    def set_id(self, id):
        self.id = id

    def get_user_profile(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + str(self.access_token)
        }

        UrlRequest(
            self.profile_url,
            on_success=self.get_profile_success,
            on_failure=self.get_profile_failure,
            req_headers=headers,
            method='POST'
        )

    def get_profile_success(self, req, result):
        profile_data = result

        self.ids.first_name_field.text = profile_data.get('Firstname', '')
        self.ids.last_name_field.text = profile_data.get('Lastname', '')
        self.ids.email_field.text = profile_data.get('email', '')
        self.ids.phone_field.text = profile_data.get('phone_number', '')
        self.ids.dob_field.text = profile_data.get('dob', '')

    def get_profile_failure(self, req, result):
        pass

    def edit_profile(self):
        first_name = self.ids.first_name_field.text
        last_name = self.ids.last_name_field.text
        email = self.ids.email_field.text
        phone_number = self.ids.phone_field.text
        dob = self.ids.dob_field.text

        payload = {
            'Firstname': first_name,
            'Lastname': last_name,
            'email': email,
            'phone_number': phone_number,
            'id': self.id,
            'dob':dob
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + str(self.access_token)
        }

        UrlRequest(
            self.edit_url,
            on_success=self.edit_profile_success,
            on_failure=self.edit_profile_failure,
            req_body=json.dumps(payload),
            req_headers=headers
        )

    def edit_profile_success(self, req, result):
        dialog = MDDialog(
            title="Success",
            text=result['message'],
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=self.dismiss_dialog
                )
            ]
        )
        dialog.open()
        self.manager.current = 'edit_profile'

    def dismiss_dialog(self, *args):
        self.manager.current = 'edit_profile'

    def edit_profile_failure(self, req, result):
        dialog = MDDialog(
            title="Error",
            text=result['message'],
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=self.dismiss_dialog
                )
            ]
        )
        dialog.open()

    def on_enter(self):
        self.get_user_profile()

    
    
    