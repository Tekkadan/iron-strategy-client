import urwid

basepalette = [
        ('banner', 'black', 'light gray', 'bold'),
        ('streak', 'black,' 'dark red'),
        ('bg', 'black', 'dark blue'),]

placeholder = urwid.SolidFill()
gameLoop = urwid.AsyncioEventLoop(placeholder, palette)
gameLoop.screen.set_terminal_properties(colors=256)
gameLoop.widget = urwid.AttrMap(placeholder, 'banner')
gameLoop.widget.base_widget = GameState(loop)
