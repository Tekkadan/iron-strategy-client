import urwid
from .play import PlayScreen

class WelcomeScreen(urwid.WidgetWrap):

    def __init__(self, game):
        super(WelcomeScreen, self).__init__(urwid.Filler(urwid.Text("Welcome on Iron Strategy!"), 'top'))
        self.game = game # now we can push PlayScreen if clicked on it

    def keypress(self, size, key):
        if key == 'p':
            self.game.game_state.push_screen(PlayScreen(self.game))

    def selectable(self):
        return True


