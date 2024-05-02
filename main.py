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
import overlays
import threading



MONTH = datetime.datetime.now().month
YEAR = datetime.datetime.now().year



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
        MONTH = self.current_month_index + 1
        
    def next_month(self, instance):
        self.current_month_index = (self.current_month_index + 1) % len(self.months)
        self.label.text = self.months[self.current_month_index]
        MONTH = self.current_month_index + 1







class YearInput(BoxLayout):
    def __init__(self, **kwargs):
        super(YearInput, self).__init__(**kwargs)
        
        self.current_year = datetime.datetime.now().year
        
        self.label = Label(text=str(self.current_year), size_hint=(1, None), height=44)
        
        prev_button = Button(text='<', size_hint=(0.3, None), height=44)
        prev_button.bind(on_release=self.prev_year)
        
        next_button = Button(text='>', size_hint=(0.3, None), height=44)
        next_button.bind(on_release=self.next_year)
        
        self.add_widget(prev_button)
        self.add_widget(self.label)
        self.add_widget(next_button)
        
    def prev_year(self, instance):
        self.current_year -= 1
        self.label.text = str(self.current_year)
        YEAR = self.current_year
        
    def next_year(self, instance):
        self.current_year += 1
        self.label.text = str(self.current_year)
        YEAR = self.current_year







class HolidayWidget(BoxLayout):
    def __init__(self, button_text='Enable/Disable', **kwargs):
        super(HolidayWidget, self).__init__(**kwargs)
        
        self.orientation = 'horizontal'

        # Create the toggle button with dynamic text
        self.toggle_button = ToggleButton(text=button_text, size_hint_y= None, height=50)
        self.toggle_button.bind(state=self.toggle_fields)
        self.add_widget(self.toggle_button)

        # Create text input fields
        self.text_input1 = TextInput(hint_text='Students 1-5', size_hint_x=1, size_hint_y= None, height=50, multiline=False)
        self.text_input2 = TextInput(hint_text='Student 6-8', size_hint_x=1, size_hint_y= None, height=50, multiline=False)
        self.reason_input = TextInput(hint_text='Reason for Holiday', size_hint_x=0, size_hint_y= None, height=50, disabled=True)

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
            

            #self.text1 = self.text_input1.text
            #self.text2 = self.text_input2.text
            #self.text_input1.text = 0
            #self.text_input2.text = 0
        else:
            self.text_input1.disabled = False
            self.text_input2.disabled = False
            self.text_input1.size_hint_x = 1
            self.text_input2.size_hint_x = 1
            self.reason_input.disabled = True
            self.reason_input.size_hint_x = None
            self.reason_input.width = 0
            #self.text1 = self.text_input1.text
            #self.text2 = self.text_input2.text










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
        self.month_input = MonthInput()
        self.month_input.bind(on_select=self.on_month_select)
        date_grid.add_widget(self.month_input)
        date_grid.add_widget(Label(text="Year:"))
        self.year_input = YearInput()
        date_grid.add_widget(self.year_input)
        layout.add_widget(date_grid)


        
        school_label = Label(text="School:", size_hint_y=None, height=50)
        layout.add_widget(school_label)

        # School Section
        school_grid = GridLayout(cols=2, size_hint_y=None, height=200)
        school_grid.add_widget(Label(text="MDM Code:"))
        self.mdm_input = TextInput(multiline=False)
        self.setup_text_input(self.mdm_input)
        school_grid.add_widget(self.mdm_input)
        school_grid.add_widget(Label(text="School Name:"))
        self.school_name_input = TextInput(multiline=False)
        self.setup_text_input(self.school_name_input)
        school_grid.add_widget(self.school_name_input)
        school_grid.add_widget(Label(text="Gram Panchayat:"))
        self.gp_input = TextInput(multiline=False)
        self.setup_text_input(self.gp_input)
        school_grid.add_widget(self.gp_input)
        school_grid.add_widget(Label(text="Block Name:"))
        self.block_input = TextInput(multiline=False)
        self.setup_text_input(self.block_input)
        school_grid.add_widget(self.block_input)
        layout.add_widget(school_grid)


        
        bank_label = Label(text="Bank:", size_hint_y=None, height=50)
        layout.add_widget(bank_label)

        # Bank Section
        bank_grid = GridLayout(cols=2, size_hint_y=None, height=200)
        bank_grid.add_widget(Label(text="Bank Name:"))
        self.bank_name_input = TextInput(multiline=False)
        self.setup_text_input(self.bank_name_input)
        bank_grid.add_widget(self.bank_name_input)
        bank_grid.add_widget(Label(text="Account Number:"))
        self.account_input = TextInput(multiline=False)
        self.setup_text_input(self.account_input)
        bank_grid.add_widget(self.account_input)
        bank_grid.add_widget(Label(text="IFSC Code:"))
        self.ifsc_input = TextInput(multiline=False)
        self.setup_text_input(self.ifsc_input)
        bank_grid.add_widget(self.ifsc_input)
        layout.add_widget(bank_grid)

        
        contacts_label = Label(text="Contacts:" , size_hint_y=None, height=50)
        layout.add_widget(contacts_label)

        
        # Contacts Section
        contacts_grid = GridLayout(cols=2, size_hint_y=None, height=200)
        contacts_grid.add_widget(Label(text="Institute Head's Number:"))
        self.head_mobile_input = TextInput(multiline=False)
        self.setup_text_input(self.head_mobile_input)
        contacts_grid.add_widget(self.head_mobile_input)
        contacts_grid.add_widget(Label(text="Whatsapp Number:"))
        self.whatsapp_input = TextInput(multiline=False)
        self.setup_text_input(self.whatsapp_input)
        contacts_grid.add_widget(self.whatsapp_input)
        layout.add_widget(contacts_grid)

        
        student_label = Label(text="Student No.:" , size_hint_y=None, height=50)
        layout.add_widget(student_label)


        # Student Number Section
        student_grid = GridLayout(cols=2, size_hint_y=None, height=200)
        student_grid.add_widget(Label(text="1 to 5:"))
        self.student_1to5_input = TextInput(multiline=False)
        self.setup_text_input(self.student_1to5_input)
        student_grid.add_widget(self.student_1to5_input)
        student_grid.add_widget(Label(text="6 to 8:"))
        self.student_6to8_input = TextInput(multiline=False)
        self.setup_text_input(self.student_6to8_input)
        student_grid.add_widget(self.student_6to8_input)
        layout.add_widget(student_grid)

        nextButton = Button(text="Next", on_press=self.change_screen, size_hint_y=None, height=50)
        layout.add_widget(nextButton)

        scrollview = ScrollView(size_hint=(1, 1))
        scrollview.add_widget(layout)
        self.add_widget(scrollview)

    def setup_text_input(self, text_input):
        text_input.bind(on_text_validate=self.move_focus_to_next_input)
        self.text_inputs.append(text_input)
        print("Focus event bound to text input")

    def move_focus_to_next_input(self,instance, *args):
        self.current_input_index = self.text_inputs.index(instance)
        self.current_input_index += 1
        while (self.current_input_index < len(self.text_inputs) and 
            self.text_inputs[self.current_input_index].disabled):
            self.current_input_index += 1
        if self.current_input_index < len(self.text_inputs):
            self.text_inputs[self.current_input_index].focus = True


    def on_month_select(self, instance, text):
        pass
        

    def change_screen(self, *args):
        self.manager.current = 'second'
        overlays.date[0][0] = f'{self.month_input.months[self.month_input.current_month_index]} {self.year_input.current_year}'
        overlays.school_data[0][0] = self.school_name_input.text
        overlays.school_data[1][0] = self.bank_name_input.text
        overlays.school_data[2][0] = self.gp_input.text
        overlays.school_data[3][0] = self.account_input.text
        overlays.school_data[4][0] = self.ifsc_input.text
        overlays.school_data[5][0] = self.block_input.text
        overlays.school_data[6][0] = self.student_1to5_input.text
        overlays.school_data[7][0] = self.student_6to8_input.text
        overlays.school_data[8][0] = self.head_mobile_input.text
        overlays.school_data[9][0] = self.whatsapp_input.text
        overlays.school_data[10][0] = self.mdm_input.text
        # Run printSchoolData directly in a separate thread
        threading.Thread(target=overlays.printSchoolData).start()











class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.text_inputs = []  # List to store TextInput widgets
        self.holiday_inputs = []
        self.current_input_index = 0  # Index of the currently focused TextInput
        
        num_days = calendar.monthrange(YEAR, MONTH)[1]
        element_height = 50
        total_height = (num_days + 3) * element_height  # +3 for the button, label, and submit button

        layout = GridLayout(cols=1, size_hint_y=None, height=total_height)

        prevButton = Button(text="Go to First Screen", size_hint_y=None, height=element_height)
        prevButton.bind(on_press=self.change_screen)
        layout.add_widget(prevButton)

        head_label = Label(text="Holidays and Present Students", size_hint_y=None, height=element_height)
        layout.add_widget(head_label)

        for i in range(num_days):
            day = i + 1
            is_sunday = datetime.date(YEAR, MONTH, day).weekday() == 6  # 6 represents Sunday
            row = HolidayWidget(button_text=f'Day {day}:')
            if is_sunday:
                row.toggle_button.state = 'down'  # Set toggleButton to pressed
                row.reason_input.text = "- - S U N D A Y - -"
            self.setup_text_input(text_input=row.text_input1)
            self.setup_text_input(text_input=row.text_input2)
            layout.add_widget(row)

        submit_button = Button(text="Submit", size_hint_y=None, height=element_height)
        submit_button.bind(on_press=self.process_input)
        layout.add_widget(submit_button)

        scrollview = ScrollView(size_hint=(1, 1), size=(400, 800))  # Adjust size as necessary
        scrollview.add_widget(layout)
        self.add_widget(scrollview)

    def setup_text_input(self, text_input):
        text_input.bind(on_text_validate=self.move_focus_to_next_input)
        self.text_inputs.append(text_input)


    def move_focus_to_next_input(self,instance, *args):
        self.current_input_index = self.text_inputs.index(instance)
        self.current_input_index += 1
        while (self.current_input_index < len(self.text_inputs) and 
            self.text_inputs[self.current_input_index].disabled):
            self.current_input_index += 1
        
        if self.current_input_index < len(self.text_inputs):
            self.text_inputs[self.current_input_index].focus = True


    def process_input(self, *args):
        text_inputs = self.text_inputs
        odd_inputs = []
        even_inputs = []

        for index, text_input in enumerate(text_inputs):
            if text_input.disabled:
                # If the text input is disabled, add 0 directly
                input_value = 0
            else:
                # Access the text property of each text input to get the input value
                input_value = text_input.text
                # Try to convert the input value to an integer
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

        print("Even indexed inputs:", even_inputs)
        print("Odd indexed inputs:", odd_inputs)
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