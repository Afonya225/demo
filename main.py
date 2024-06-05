from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDTimePicker
# from kivymd.theming import ColorProperty
# from kivymd.uix.button import MDIconButton
# from kivymd.uix.button import MDRaisedButton
# from kivymd.uix.button import MDTextButton
# from kivymd.uix.button import MDFlatButton

class Coin (FloatLayout):

    def show_time_picker(self):
        time_picker = MDTimePicker()
        time_picker.open()

    def show_date_picker(self):
        time_picker = MDDatePicker()
        time_picker.open()

    def calculate(self, in_start_time=None, in_finish_time=None):
        input_time = str(in_finish_time)+str(in_start_time)
        self.ids.LB_result.text = input_time

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Coin()




#d

if __name__ == "__main__":
    MyApp().run()

