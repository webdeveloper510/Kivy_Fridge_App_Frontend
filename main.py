from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.config import Config
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget
from kivy.properties import ListProperty
import numpy as np
from kivy_garden.zbarcam import ZBarCam
import requests
from kivymd.uix.pickers import MDDatePicker
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
Window.size = (360,650)

class SplashScreen(MDScreen):
    def on_enter(self):
        
        Clock.schedule_once(self.switch_to_login, 20)

    def switch_to_login(self, dt):
        self.manager.current = 'login'


class LoginScreen(MDScreen):
    def toggle_password_visibility(self):
        password_field = self.root.ids.password_field
        password_field.password = not password_field.password
        password_field.icon_right = "eye" if password_field.password else "eye-off"
    
    
    def login(self, email, password):
        pass
    
    

class RegisterScreen(MDScreen):
    pass

class EditProfileScreen(MDScreen):
    pass

class ForgetPasswordScreen(MDScreen):
    pass

class ResetPasswordScreen(MDScreen):
    pass

class ScannerScreen(MDScreen):
    pass

class SettingsScreen(MDScreen):
    pass

class BottomNavigation(BoxLayout):
    pass

class MDDialogBox(MDDialog):
    pass


class NotificationDetails(MDBoxLayout):
    pass


class NotificationScreen(MDScreen):
    def on_pre_enter(self):
        # Add some example notifications to the list
        for i in range(10):
            item = OneLineListItem(text=f'Notification {i}')
            item.notification_title = f'Title {i}'
            item.notification_text = f'This is notification {i}.'
            item.bind(on_release=self.show_notification_details)
            self.ids.notification_list.add_widget(item)

    def show_notification_details(self, item):
        # Create a dialog box to display the details of the selected notification
        dialog = MDDialog(
            title=item.notification_title,
            text=item.notification_text,
            size_hint=(0.8, 0.8),
            auto_dismiss=False,
            buttons=[
            MDFlatButton(
                text="Close",
                on_release=lambda *args: dialog.dismiss()  # Add a button that dismisses the dialog when pressed
            )
        ]
         )
        dialog.open()


class CustomListItem(OneLineListItem):
    pass


class ListDialog(MDDialog):
    pass


class FoodTrack(Screen):
    def show_dialog(self, button_text):
        if button_text == "Green Button Clicked":
            items = ["Green Item 1", "Green Item 2", "Green Item 3"]# create custom items later get data from source 
            dialog = ListDialog()

            for item in items:
                dialog.ids.list_content.add_widget(CustomListItem(text=item))

            dialog.open()
        elif button_text == "Amber Button Clicked":
            items = ["Amber Item 1", "Amber Item 2", "Amber Item 3"]# create  static data  later get data from source
            dialog = ListDialog()

            for item in items:
                dialog.ids.list_content.add_widget(CustomListItem(text=item))

            dialog.open()
        elif button_text == "Red Button Clicked":
            items = ["Red Item 1", "Red Item 2", "Red Item 3"]
            dialog = ListDialog()

            for item in items:
                dialog.ids.list_content.add_widget(CustomListItem(text=item))

            dialog.open()

class HomeScreen(MDScreen):
 pass

class FoodHygiene(MDScreen):
  pass

class MyScreenManager(ScreenManager):
    pass



class FridgeApp(MDApp):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(EditProfileScreen(name='edit_profile'))
        sm.add_widget(ResetPasswordScreen(name='reset_password'))
        sm.add_widget(ForgetPasswordScreen(name='forget_password'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ScannerScreen(name='scanner'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(NotificationScreen(name='notifications'))
        sm.add_widget(FoodHygiene(name='fridge_hygiene'))
        sm.add_widget(FoodTrack(name="FoodTrack"))

        return sm
   
    
    
if __name__ == '__main__':
    FridgeApp().run()
