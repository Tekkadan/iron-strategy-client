import urwid
from .play import PlayScreen

class WelcomeScreen(urwid.WidgetWrap):

    def __init__(self, game):
        super(WelcomeScreen, self).__init__(self.build())
        self.game = game # now we can push PlayScreen if clicked on it

    def keypress(self, size, key):
        if key == 'p':
            self.game.game_state.push_screen(PlayScreen(self.game))
        elif key == 'q':
            self.game.exitMainLoop()

    def selectable(self):
        return True

    def build(self):
        return urwid.Filler(
            urwid.Text('Welcome to Iron Strategy ! Press P to begin.', align='center'),
            'middle'
        )
