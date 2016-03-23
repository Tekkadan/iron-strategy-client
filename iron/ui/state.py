import urwid

class StateManager(urwid.WidgetWrap):
    def __init__(self, game, screen):
        super(StateManager, self).__init__(screen)
        self.state = [screen]

        self._show_stack()

    def _show_stack(self):
        print ('Stack screen: {} (last is the first to be depopped)'\
               .format(' --> '.join(map(str, self.state))))

    def push_screen(self, screen):
        self.state.append(screen)
        self._show_stack()

    def pop_screen(self):
        self.state.pop()
        self._w = self.peek()
        self._show_stack()

    def peek(self):
        return self.state[0]
