import urwid

class Menu(urwid.Widget):
    _sizing = frozenset(['box'])
    menu = []

    def __init__(self, **kwargs):
        for btnname, scene in kwargs.iteritems():
            button = urwid.Button(btnname)
            menu.append(urwid.AttrMap(button, None, focus_map='inverted'))

    def render(self, size, focus=False):
        (maxcol, maxrow) = size
        return urwid.TextCanvas(urwid.ListBox(urwid.SimpleFocusListWalker(self.menu))



