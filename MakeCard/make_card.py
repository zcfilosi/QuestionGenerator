from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup


class card_button(ListItemButton):
    pass

class make_card_gui(BoxLayout):
    front_text_input = ObjectProperty(None)
    back_text_input = ObjectProperty(None)
    card_list = ObjectProperty(None)

    def create_card(self, *args): #  create the popup
        pass
    def submit_card(self, *args): #  within popup, for submission
        pass
    def view_card(self, *args): #  create new popup showing card contents
        pass

class  make_card_guiApp(App):
    def build(self):
        return make_card_gui()

if __name__== "__main__":
    card = make_card_guiApp()
    card.run()
