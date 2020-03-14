from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from souppy_oh.request import requester

class SearchScreen(GridLayout):

    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.row_default_height = 40
        self.row_force_default = True
        self.orientation = 'vertical'

        label = Label(text='[i][b][size=40][color=3394FF]Enter a '
                           'stock and hit '
                           'submit[/i][/b][/size][/color]\nor\n '
                           '[size=40][i][b][color=3394FF]Enter a stock and '
                           'hit enter '
                           'in the '
                           'textbox[/i][/b][/size][/color]',
                      halign='center', markup=True)
        self.add_widget(label)
        self.search = TextInput(multiline=False)
        self.search.bind(on_text_validate=self.on_enter)
        self.add_widget(self.search)

        enter = Button(text='Submit')
        enter.bind(on_press=self.on_submit)
        self.add_widget(enter)

        # textinput = TextInput()
        # textinput.bind(text=SearchScreen.on_text)
        # self.add_widget(textinput)

        self.row_force_default = False
        self.stock_info = Label(halign='left', valign='bottom', height=200)
        self.add_widget(self.stock_info)

    def on_enter(self, instance):
        if self.search.text == '':
            self.stock_info.text = 'Invalid input'
        else:
            self.stock_info.text = requester.get_stock_data_str(
                instance.text)

    def on_submit(self):
        if self.search.text == '':
            self.stock_info.text = 'Invalid input'
        else:
            self.stock_info.text = requester.get_stock_data_str(
                self.search.text)

    # for testing
    # def on_text(self, instance, value):
    #     print('The widget', instance, 'have:', value)


class MyApp(App):
    def build(self):
        return SearchScreen()


if __name__ == '__main__':
    MyApp().run()
