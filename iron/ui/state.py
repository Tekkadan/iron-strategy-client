import urwid

class StateManager(urwid.WidgetWrap):
    def __init__(self, game, screen):
        super(StateManager, self).__init__(screen)
        self.state = [screen]

    def push_screen(self, screen):
        self.state.append(screen)

    def pop_screen(self):
        self.state.pop()
        self._w = self.peek()

    def peek(self):
        return self.state[0]
