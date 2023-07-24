from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.list import TwoLineListItem

class ExpiryItemScreen(Screen):
      def __init__(self, **kwargs):
        super(ExpiryItemScreen, self).__init__(**kwargs)
        self.request = None
        self.id = None 
      
      def set_id(self, id):
         self.id = id
         self.url ='http://127.0.0.1:8000/expirydateitems/{}/'.format(self.id)

      def get_expiry_item(self):
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
          expirydata=result
          self.ids.container.clear_widgets()
          for expiry_item_data in expirydata:
             
              self.ids.container.add_widget(
                            TwoLineListItem(text=expiry_item_data['food_name'],secondary_text="Expiry item")
                        )
      
      def on_failure(self, req, result):
          pass

      def on_enter(self):
        self.get_expiry_item()