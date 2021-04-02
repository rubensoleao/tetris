import curses

def init():
    global stdscr
    stdscr = curses.initscr()


def config():
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    stdscr.nodelay(True)
    stdscr.keypad(True)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)



def deconfig():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()


def kill():
    curses.endwin()
