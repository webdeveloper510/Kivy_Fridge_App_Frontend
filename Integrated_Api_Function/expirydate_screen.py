from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivy.network.urlrequest import UrlRequest
from kivy.utils import get_color_from_hex
import json
from kivy.properties import ListProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from Integrated_Api_Function.url import Base_Url

class ExpiryDateScreen(Screen):
    def __init__(self, **kwargs):
        super(ExpiryDateScreen, self).__init__(**kwargs)
        item_ids = ListProperty([])
        items = ListProperty([])

    def set_itemid(self, item_ids):
        self.item_ids = item_ids

    def set_itemlist(self, items):
        self.items = items

    def on_pre_enter(self):
        grid_layout = self.ids.grid_layout
        grid_layout.clear_widgets()

        for i, item_id in enumerate(self.item_ids):
            label_text = self.items[i]
            label = MDLabel(
                text=label_text,
                halign="center",
                valign="center",
                size_hint_x=None,
                width="120dp",
            )
            grid_layout.add_widget(label)
            text_input = MDTextField(
                halign="left",
                hint_text="YYYY-MM-DD",
            )
            grid_layout.add_widget(text_input)
            # print("kkkkkkk------>",self.items[i])

    def update_data(self):
        data = {
            "data": [] 
        }
        grid_layout = self.ids.grid_layout

        for i, item_id in enumerate(self.item_ids):
            label_text = grid_layout.children[i * 2].text
            for child in grid_layout.children:
                if isinstance(child, MDTextField) and child.text == label_text:
                    expiry_date = child.text
                    data["data"].append({"id": item_id, "expiry_date": expiry_date})  # Add data to the "data" key
                    break

        json_data = json.dumps(data).encode("utf-8")
        headers = {"Content-Type": "application/json"}

        req = UrlRequest(
            url='{}/update_food_item/'.format(Base_Url),
            req_body=json_data,
            req_headers=headers,
            on_success=self.handle_success,
            on_failure=self.handle_failure,
        )


    def handle_success(self, req, result):
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
        self.manager.current ='home'

    def handle_failure(self, req, result):
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
        self.manager.current = 'expiry_screen'
    
   


