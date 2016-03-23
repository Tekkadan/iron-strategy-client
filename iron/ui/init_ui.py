import urwid
from iron.ui.state import StateManager

basepalette = [
    ('banner', 'black', 'light gray', 'bold'),
    ('streak', 'black,' 'dark red'),
    ('bg', 'black', 'dark blue'),]

def ui_init():
    placeholder = urwid.SolidFill()
    gameLoop = urwid.AsyncioEventLoop()
    gameLoop.widget = StateManager('initial')

    gameLoop.run()

