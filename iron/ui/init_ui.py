import urwid
import asyncio
from iron.ui.state import StateManager
from iron.screens.welcome import WelcomeScreen

basepalette = [
    ('banner', 'black', 'light gray', 'bold'),
    ('streak', 'black,' 'dark red'),
    ('bg', 'black', 'dark blue'),]

class Application:

    def __init__(self):
        self.game_state = StateManager(self, WelcomeScreen(self))
        self.evl = urwid.AsyncioEventLoop(loop=asyncio.get_event_loop())
        self.loop = urwid.MainLoop(self.game_state, event_loop=self.evl)

    def start(self):
        self.loop.run()
        return self

def ui_init():
    return Application().start()
