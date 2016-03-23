import urwid

class PlayScreen(urwid.WidgetWrap):
    def __init__(self, game):
        super(PlayScreen, self).__init__(self.build())
        self.game = game

    def selectable(self):
        return True

    def keypress(self, size, key):
        if key == 'q':
            self.game.game_state.pop_screen()

    def build(self):
        return urwid.Filler(
            urwid.Text("You're going to play to Iron Strategy, you're thrilled, right?"),
            "top"
        )
