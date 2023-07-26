from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.list import TwoLineListItem
from Integrated_Api_Function.url import Base_Url


class GreenItemScreen(Screen):
    def __init__(self, **kwargs):
        super(GreenItemScreen, self).__init__(**kwargs)
        self.request = None
        self.id = None 


    def set_id(self, id):
         self.id = id
         self.url ='{}/greenIndateitems/{}/'.format(Base_Url,self.id)
     
    def get_green_item(self):
         headers = {
            'Content-Type': 'application/json',
        }
         UrlRequest(
               self.url,
               on_success=self.on_success,
               on_failure=self.on_failure,
               req_headers=headers,
               method='GET'
         )
        
    def on_success(self, req, result):
          itemdata=result
          self.ids.container.clear_widgets()
          for green_item_data in itemdata:
              self.ids.container.add_widget(
                            TwoLineListItem(text=green_item_data['food_name'],secondary_text=green_item_data['date'])
                        )
      
    def on_failure(self, req, result):
         pass

    def on_enter(self):
        self.get_green_item()