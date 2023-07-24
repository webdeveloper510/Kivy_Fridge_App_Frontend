from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.list import OneLineListItem

class UseByDateItemScreen(Screen):
      def __init__(self, **kwargs):
        super(UseByDateItemScreen, self).__init__(**kwargs)
        self.request = None
        self.id = None 

      def set_id(self, id):
         self.id = id
         self.url ='http://127.0.0.1:8000/usebydate/{}/'.format(self.id)
      
      def get_UseBy_item(self):
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
          for Use_item_data in itemdata:
              self.ids.container.add_widget(
                            OneLineListItem(text=Use_item_data['food_name'])
                        )
      
      def on_failure(self, req, result):
          print(result)

      def on_enter(self):
        self.get_UseBy_item()