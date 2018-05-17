import math
import curses

COLOR_THEME = [
    # (foreground, background)
    (curses.COLOR_BLACK, curses.COLOR_BLACK),   #0
    (curses.COLOR_WHITE, curses.COLOR_BLACK),   #2
    (curses.COLOR_YELLOW, curses.COLOR_BLACK),  #4
    (curses.COLOR_RED, curses.COLOR_BLACK),     #8
    (curses.COLOR_MAGENTA, curses.COLOR_BLACK), #16
    (curses.COLOR_BLUE, curses.COLOR_BLACK),    #32
    (curses.COLOR_CYAN, curses.COLOR_BLACK),    #64
    (curses.COLOR_GREEN, curses.COLOR_BLACK),   #128
    (curses.COLOR_YELLOW, curses.COLOR_WHITE),  #256
    (curses.COLOR_RED, curses.COLOR_WHITE),     #512 
    (curses.COLOR_MAGENTA, curses.COLOR_WHITE), #1024
    (curses.COLOR_BLUE, curses.COLOR_WHITE),    #2048
]


for i, color_pair in enumerate(COLOR_THEME):
    n = 2**i
    print(n, color_pair)
    print(int(math.log(n, 2)))



