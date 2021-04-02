import curses

def init():
    global stdscr
    stdscr = curses.initscr()


def config():
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(True)
    stdscr.keypad(True)


def deconfig():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()


def kill():
    curses.endwin()
