from iexfinance.utils.exceptions import IEXQueryError
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from souppy_oh.request import requester

class SearchScreen(GridLayout):

    tickers = (lambda f: open(f).read())('symbols.csv').split()

    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.row_default_height = 20
        # self.row_force_default = True
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

        enter = Button(text='Search')
        enter.bind(on_press=self.on_enter)
        self.add_widget(enter)

        # self.row_force_default = False
        self.stock_info = Label(halign='left', valign='bottom', text='STONKS')
        self.add_widget(self.stock_info)

    def on_enter(self, instance):
        if self.search.text.upper() not in self.tickers:
            self.stock_info.text = '$' + self.search.text.upper() + ' is an invalid ticker'
        else:
            self.stock_info.text = 'Market Data for $' + \
                          self.search.text.upper() + ': \n\n' + \
                      requester.get_stock_data_str(self.search.text)


class MyApp(App):
    def build(self):
        return SearchScreen()


if __name__ == '__main__':
    MyApp().run()
