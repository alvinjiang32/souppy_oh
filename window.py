from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from souppy_oh.request import requester

class SearchScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        label = Label(text='Stock Name')
        self.add_widget(label)
        search = TextInput(multiline=False)
        search.bind(on_text_validate=SearchScreen.on_enter)
        self.add_widget(search)
        enter = Button(text='Submit')
        self.add_widget(enter)

        textinput = TextInput()
        textinput.bind(text=SearchScreen.on_text)
        self.add_widget(textinput)

        stock_info = Label()
        self.add_widget(stock_info)

        self.orientation = 'vertical'

    def on_enter(self, instance):
        self.stock_info.text = requester.get_stock_data()

    @staticmethod
    def on_text(instance, value):
        print('The widget', instance, 'have:', value)

    @staticmethod
    def get_stock_info(value):
        requester.get_stock_data(value)

    @staticmethod
    def on_focus(instance, value):
        if value:
            print('User focused', instance)
        else:
            print('User de-focused', instance)


class MyApp(App):
    def build(self):
        return SearchScreen()


if __name__ == '__main__':
    MyApp().run()
