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

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)



def deconfig():
    curses.echo() # removes noecho
    curses.nocbreak() # removes Cbreak
    #nocolor
    stdscr.keypad(False)
    stdscr.nodelay(False)
    curses.curs_set(1) # curs_set(0)


def kill():
    curses.endwin()
