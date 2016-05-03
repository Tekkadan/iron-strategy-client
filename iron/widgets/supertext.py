from urwid import Text
from pyfiglet import figlet_format

class Supertext(Text):
    def get_text():
        return('\n'+figlet_format(self.markup, font='banner3'))
