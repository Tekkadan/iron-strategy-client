import urwid

from pyfiglet import figlet_format
from .play import PlayScreen

class WelcomeScreen(urwid.WidgetWrap):

    def __init__(self, game):
        super(WelcomeScreen, self).__init__(self.build())
        self.game = game # now we can push PlayScreen if clicked on it

    def keypress(self, size, key):
        if key == 'q':
            self.game.quit()
        else:
            self.game.game_state.push_screen(PlayScreen(self.game))

    def selectable(self):
        return True

    def build(self):
        return urwid.AttrMap(urwid.Filler(
                urwid.AttrMap(urwid.Text('\n{}\n\n Press any key to continue.\n\n'.format(figlet_format('IRON STRATEGY', font='banner3')), align='center'), 'banner')), 'bg')
