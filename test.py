from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput

class HolidayWidget(BoxLayout):
    def __init__(self, button_text='Enable/Disable', **kwargs):
        super(HolidayWidget, self).__init__(**kwargs)
        
        self.orientation = 'horizontal'

        # Create the toggle button with dynamic text
        self.toggle_button = ToggleButton(text=button_text)
        self.toggle_button.bind(state=self.toggle_fields)
        self.add_widget(self.toggle_button)

        # Create text input fields
        self.text_input1 = TextInput(text='Field 1', size_hint_x=1)
        self.text_input2 = TextInput(text='Field 2', size_hint_x=1)
        self.reason_input = TextInput(hint_text='Reason for Holiday', size_hint_x=1, disabled=True)

        # Add text inputs to the layout
        self.add_widget(self.text_input1)
        self.add_widget(self.text_input2)
        self.add_widget(self.reason_input)

    def toggle_fields(self, instance, value):
        if value == 'down':
            self.text_input1.disabled = True
            self.text_input2.disabled = True
            self.text_input1.size_hint_x = None
            self.text_input2.size_hint_x = None
            self.text_input1.width = 0
            self.text_input2.width = 0
            self.reason_input.disabled = False
            self.reason_input.size_hint_x = 1
        else:
            self.text_input1.disabled = False
            self.text_input2.disabled = False
            self.text_input1.size_hint_x = 1
            self.text_input2.size_hint_x = 1
            self.reason_input.disabled = True
            self.reason_input.size_hint_x = None
            self.reason_input.width = 0


class TestApp(App):
    def build(self):
        # You can now specify the button text when creating a HolidayWidget instance
        return HolidayWidget(button_text='Toggle Inputs')


if __name__ == '__main__':
    TestApp().run()
