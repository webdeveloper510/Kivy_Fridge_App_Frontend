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

# from kivy.core.window import Window
# Window.size = (450, 500)

class SplashScreen(Screen):
    def on_enter(self):
        anim = Animation(size_hint=(1.1, 1.1), duration=1)
        # Start the animation on the screen
        anim.start(self)
        Clock.schedule_once(self.switch_to_login, 3)

    def switch_to_login(self, dt):
        self.manager.current = 'login'


class LoginScreen(Screen):
    def login(self, email, password):
        pass
    

class RegisterScreen(Screen):
    def register(self, first_name, last_name, password, confirm_password,
                 dob, phone, clubcard):
        print(f"Registering {first_name} {last_name} with password {password}, "
              f"DOB: {dob}, Phone: {phone}, Clubcard: {clubcard}")
        # self.manager.current = 'login'

class EditProfileScreen(Screen):
    pass

class ForgetPasswordScreen(Screen):
    pass

class ResetPasswordScreen(Screen):
    pass

class ScannerScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class BottomNavigation(BoxLayout):
    pass


class MDDialogBox(MDDialog):
    pass


class NotificationDetails(MDBoxLayout):
    pass


class NotificationScreen(Screen):
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

class HomeScreen(Screen):
  pass


class FoodHygiene(Screen):
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
        return sm
    
    def clear_notifications(self):
        print('Clearing notifications...')
    
    def callback(self, instance_action_top_appbar_button):
        print(instance_action_top_appbar_button)
    
if __name__ == '__main__':
    FridgeApp().run()
