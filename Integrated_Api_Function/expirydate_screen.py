from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
import json

class ExpiryDateScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(ExpiryDateScreen, self).__init__(**kwargs)
        self.orientation = "vertical"

        top_app_bar = MDTopAppBar(title="Expiry Date")
        self.add_widget(top_app_bar)

        grid_layout = GridLayout(cols=2, spacing="10dp", padding="10dp")
        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        for i, item_id in enumerate(self.item_ids):
            label_text = self.items[i]  # Get the item name from set_itemlist
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
                hint_text="YYYY/MM/DD",
                text=self.items[i],  # Set the initial text from item list
            )
            grid_layout.add_widget(text_input)

        scroll_view = ScrollView()
        scroll_view.add_widget(grid_layout)
        self.add_widget(scroll_view)

        grid_layout.bind(minimum_height=grid_layout.setter("height"))
        grid_layout.size_hint_y = None
        grid_layout.height = grid_layout.minimum_height

        update_button = MDFlatButton(
            text="Update",
            halign="center",
            pos_hint={"center_x": 0.5},
            md_bg_color=get_color_from_hex("#258fff"),
        )
        update_button.bind(on_release=self.update_data)
        self.add_widget(update_button)

    def set_itemid(self, item_ids):
        self.item_ids = item_ids

    def set_itemlist(self, items):
        self.items = items

    def update_data(self, instance):
        data = []
        for i, item_id in enumerate(self.item_ids):
            label_text = self.children[0].children[i].children[0].text
            expiry_date = self.children[0].children[i].children[1].text  # Get expiry date from text input
            data.append({"id": item_id, "expiry_date": expiry_date})

        json_data = json.dumps(data).encode("utf-8")
        headers = {"Content-Type": "application/json"}

        req = UrlRequest(
            url='http://127.0.0.1:8000/update_food_item/',
            req_body=json_data,
            req_headers=headers,
            on_success=self.handle_success,
            on_failure=self.handle_failure,
        )

    def handle_success(self, req, result):
        print("sucess")

    def handle_failure(self, req, result):
        print("Failed to update data")