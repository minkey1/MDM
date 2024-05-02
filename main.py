from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
import calendar
import datetime

class MonthInput(BoxLayout):
    def __init__(self, **kwargs):
        super(MonthInput, self).__init__(**kwargs)
        
        self.current_month_index = datetime.datetime.now().month - 1
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        self.label = Label(text=self.months[self.current_month_index], size_hint=(1, None), height=44)
        
        prev_button = Button(text='<', size_hint=(0.3, None), height=44)
        prev_button.bind(on_release=self.prev_month)
        
        next_button = Button(text='>', size_hint=(0.3, None), height=44)
        next_button.bind(on_release=self.next_month)
        
        self.add_widget(prev_button)
        self.add_widget(self.label)
        self.add_widget(next_button)
        
    def prev_month(self, instance):
        self.current_month_index = (self.current_month_index - 1) % len(self.months)
        self.label.text = self.months[self.current_month_index]
        
    def next_month(self, instance):
        self.current_month_index = (self.current_month_index + 1) % len(self.months)
        self.label.text = self.months[self.current_month_index]


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.text_inputs = []  # List to store TextInput widgets
        self.current_input_index = 0  # Index of the currently focused TextInput

        
        layout = GridLayout(cols=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Date Section
        date_label = Label(text="Date:", size_hint_y=None, height=50)
        layout.add_widget(date_label)

        date_grid = GridLayout(cols=2, size_hint_y=None, height=100)
        date_grid.add_widget(Label(text="Month:"))
        month_input = MonthInput()
        month_input.bind(on_select=self.on_month_select)
        date_grid.add_widget(month_input)
        date_grid.add_widget(Label(text="Year:"))
        year_input = TextInput(input_filter="int", multiline=False, input_type="number")
        year_input.bind(on_text_validate=lambda instance: self.move_focus_to_next_input(year_input))
        self.text_inputs.append(year_input)
        date_grid.add_widget(year_input)
        layout.add_widget(date_grid)


        
        school_label = Label(text="School:", size_hint_y=None, height=50)
        layout.add_widget(school_label)

        # School Section
        school_grid = GridLayout(cols=2, size_hint_y=None, height=200)
        school_grid.add_widget(Label(text="MDM Code:"))
        mdm_input = TextInput()
        self.text_inputs.append(mdm_input)
        school_grid.add_widget(mdm_input)
        school_grid.add_widget(Label(text="School Name:"))
        school_name_input = TextInput()
        self.text_inputs.append(school_name_input)
        school_grid.add_widget(school_name_input)
        school_grid.add_widget(Label(text="Gram Panchayat:"))
        gp_input = TextInput()
        self.text_inputs.append(gp_input)
        school_grid.add_widget(gp_input)
        school_grid.add_widget(Label(text="Block Name:"))
        block_input = TextInput()
        self.text_inputs.append(block_input)
        school_grid.add_widget(block_input)
        layout.add_widget(school_grid)


        
        bank_label = Label(text="Bank:", size_hint_y=None, height=50)
        layout.add_widget(bank_label)

        # Bank Section
        bank_grid = GridLayout(cols=2, size_hint_y=None, height=200)
        bank_grid.add_widget(Label(text="Bank Name:"))
        bank_name_input = TextInput()
        self.text_inputs.append(bank_name_input)
        bank_grid.add_widget(bank_name_input)
        bank_grid.add_widget(Label(text="Account Number:"))
        account_input = TextInput()
        self.text_inputs.append(account_input)
        bank_grid.add_widget(account_input)
        bank_grid.add_widget(Label(text="IFSC Code:"))
        ifsc_input = TextInput()
        self.text_inputs.append(ifsc_input)
        bank_grid.add_widget(ifsc_input)
        layout.add_widget(bank_grid)

        
        contacts_label = Label(text="Contacts:" , size_hint_y=None, height=50)
        layout.add_widget(contacts_label)

        
        # Contacts Section
        contacts_grid = GridLayout(cols=2, size_hint_y=None, height=200)
        contacts_grid.add_widget(Label(text="Institute Head's Number:"))
        head_mobile_input = TextInput()
        self.text_inputs.append(head_mobile_input)
        contacts_grid.add_widget(head_mobile_input)
        contacts_grid.add_widget(Label(text="Whatsapp Number:"))
        whatsapp_input = TextInput()
        self.text_inputs.append(whatsapp_input)
        contacts_grid.add_widget(whatsapp_input)
        layout.add_widget(contacts_grid)

        
        student_label = Label(text="Student No.:" , size_hint_y=None, height=50)
        layout.add_widget(student_label)


        # Student Number Section
        student_grid = GridLayout(cols=2, size_hint_y=None, height=200)
        student_grid.add_widget(Label(text="1 to 5:"))
        student_1to5_input = TextInput()
        self.text_inputs.append(student_1to5_input)
        student_grid.add_widget(student_1to5_input)
        student_grid.add_widget(Label(text="6 to 8:"))
        student_6to8_input = TextInput()
        self.text_inputs.append(student_6to8_input)
        student_grid.add_widget(student_6to8_input)
        layout.add_widget(student_grid)

        nextButton = Button(text="Next", on_press=self.change_screen, size_hint_y=None, height=50)
        layout.add_widget(nextButton)

        scrollview = ScrollView(size_hint=(1, 1))
        scrollview.add_widget(layout)
        self.add_widget(scrollview)


    def move_focus_to_next_input(self):
        self.current_input_index += 1
        if self.current_input_index < len(self.text_inputs):
            self.text_inputs[self.current_input_index].focus = True

    def on_month_select(self, instance, text):
        # This method will be called when a month is selected from the dropdown
        pass

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)
        Window.bind(on_key_down=self.on_keyboard_down)

    def on_keyboard_down(self, window, key, *args):
        if key == 13:  # 13 is the keycode for Enter key
            self.move_focus_to_next_input()
            return True
        return False

    def change_screen(self, *args):
        self.manager.current = 'second'


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.text_inputs = []  # List to store TextInput widgets
        self.current_input_index = 0  # Index of the currently focused TextInput

        
        layout = GridLayout(cols=1, size_hint_y=None)

        prevButton = Button(text="Go to First Screen", on_press=self.change_screen, size_hint_y=None, height=50)
        layout.add_widget(prevButton)

        # Date Section
        head_label = Label(text="Holidays and Present Students", size_hint_y=None, height=50)
        layout.add_widget(head_label)

        for i in range(calendar.monthrange(year=2004, month=10)[1]):
            date_grid = GridLayout(cols=3, size_hint_y=None, height=50)
            date_grid.add_widget(ToggleButton(text=f"Day {i+1}:", size_hint_y=None, height=50))
            input1to5 = TextInput(hint_text="Students(1 - 5)", multiline=False, input_type="number", input_filter="int", size_hint_y= None, height= 50)
            date_grid.add_widget(input1to5)
            self.text_inputs.append(input1to5)

            input6to8 = TextInput(hint_text="Students(6 - 8)", multiline=False, input_type="number", input_filter="int", size_hint_y= None, height= 50)


            date_grid.add_widget(input6to8)
            self.text_inputs.append(input6to8)
            layout.add_widget(date_grid)
        
        button = Button(text="Submit", size_hint_y=None, height=50, on_press=self.process_input)
        layout.add_widget(button)

        layout.bind(minimum_height=layout.setter('height'))
        scrollview = ScrollView(size_hint=(1, 1))
        scrollview.add_widget(layout)
        self.add_widget(scrollview)


    def move_focus_to_next_input(self):
        self.current_input_index += 1
        if self.current_input_index < len(self.text_inputs):
            self.text_inputs[self.current_input_index].focus = True

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)
        Window.bind(on_key_down=self.on_keyboard_down)

    def on_keyboard_down(self, window, key, *args):
        if key == 13:  # 13 is the keycode for Enter key
            self.move_focus_to_next_input()
            return True
        return False

    def process_input(self, *args):
        text_inputs = self.text_inputs
        odd_inputs = []
        even_inputs = []

        for index, text_input in enumerate(text_inputs):
            # Access the text property of each text input to get the input value
            input_value = text_input.text
            # Convert the input value to an integer
            try:
                input_value = int(input_value)
            except ValueError:
                # Handle the case where input is not a valid integer
                input_value = 0  # or any other default value you prefer

            # Append the input value to the appropriate list based on index
            if index % 2 == 0:  # even index
                even_inputs.append(input_value)
            else:
                odd_inputs.append(input_value)
        print("1-5 inputs:", even_inputs)
        print("6-8 inputs:", odd_inputs)
        return even_inputs, odd_inputs


    def change_screen(self, *args):
        self.manager.current = 'first'

    


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm


if __name__ == '__main__':
    MyApp().run()