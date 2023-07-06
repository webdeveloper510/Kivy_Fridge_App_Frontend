from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.properties import ListProperty
from kivy_garden.zbarcam import ZBarCam
from kivymd.uix.pickers import MDDatePicker
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
Window.size = (360,650)
from Integrated_Api_Function.register import RegisterScreen
from Integrated_Api_Function.login import LoginScreen
from Integrated_Api_Function.user_profile import EditProfileScreen
from Integrated_Api_Function.forgetpassword import ForgetPasswordScreen
from Integrated_Api_Function.validateotp import OTPScreen
from Integrated_Api_Function.reset_password import ResetPasswordScreen
from Integrated_Api_Function.camera import MyCamera
# from Integrated_Api_Function.expirydate_screen import ExpiryDateScreen
from Food_Agency.Avoiding_crosscontamination import Screen1
from Food_Agency.Chilling import Chilling
from Food_Agency.cleaning import Cleaning
from Food_Agency.cooking_food import Cooking_Food
from Food_Agency.fact_checker import Fact_Checker



class SplashScreen(MDScreen):
    def on_enter(self):
        
        Clock.schedule_once(self.switch_to_login, 4)

    def switch_to_login(self, dt):
        self.manager.current = 'login'

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
        #  some example notifications to the list
        for i in range(10):
            item = OneLineListItem(text=f'Notification {i}')
            item.notification_title = f'Title {i}'
            item.notification_text = f'This is notification {i}.'
            item.bind(on_release=self.show_notification_details)
            self.ids.notification_list.add_widget(item)

    def show_notification_details(self, item):
       
        dialog = MDDialog(
            title=item.notification_title,
            text=item.notification_text,
            size_hint=(0.8, 0.8),
            auto_dismiss=False,
            buttons=[
            MDFlatButton(
                text="Close",
                on_release=lambda *args: dialog.dismiss() 
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
            items = ["Green Item 1", "Green Item 2", "Green Item 3"]# create  static data  later get data from source
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
            items = ["Red Item 1", "Red Item 2", "Red Item 3"]# create  static data  later get data from source
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
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(EditProfileScreen(name='edit_profile'))
        sm.add_widget(ResetPasswordScreen(name='reset_password'))
        sm.add_widget(OTPScreen(name='OTP_Screen'))
        sm.add_widget(ForgetPasswordScreen(name='forget_password'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(MyCamera(name='camera'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(NotificationScreen(name='notifications'))
        sm.add_widget(FoodHygiene(name='fridge_hygiene'))
        sm.add_widget(FoodTrack(name="FoodTrack"))
        sm.add_widget(Screen1(name="screen1"))
        sm.add_widget(Chilling(name="chilling"))
        sm.add_widget(Cleaning(name="cleaning"))
        sm.add_widget(Cooking_Food(name="cooking_food"))
        sm.add_widget(Fact_Checker(name="fact_checker"))
        # sm.add_widget(ExpiryDateScreen(name="expiry_screen"))
        return sm
   
    
    
if __name__ == '__main__':
    FridgeApp().run()
