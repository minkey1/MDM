from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MonthInput(BoxLayout):
    def __init__(self, **kwargs):
        super(MonthInput, self).__init__(**kwargs)
        
        self.current_month_index = 0
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        self.label = Label(text=self.months[self.current_month_index], size_hint=(1, None), height=44)
        
        prev_button = Button(text='< Prev', size_hint=(0.3, None), height=44)
        prev_button.bind(on_release=self.prev_month)
        
        next_button = Button(text='Next >', size_hint=(0.3, None), height=44)
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

class MonthInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Create MonthInput widget
        month_input = MonthInput()
        
        layout.add_widget(month_input)
        
        return layout

if __name__ == '__main__':
    MonthInputApp().run()
