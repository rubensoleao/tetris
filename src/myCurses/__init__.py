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
    curses.curs_set(0)

    define_colorsets()


def define_colorsets():
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_BLACK)



def deconfig():
    curses.echo() # removes noecho
    curses.nocbreak() # removes Cbreak
    #nocolor
    stdscr.keypad(False)
    stdscr.nodelay(False)
    curses.curs_set(1) # curs_set(0)


def kill():
    curses.endwin()
