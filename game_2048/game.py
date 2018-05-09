import curses

class Game:
    def __init__(self):
        self.matrix = [[0 for x in range(4)]for y in range(4)]
        self.score = 0
        self.moves = 0

        def move_left(self):
            raise NotImplementedError

        def move_right(self):
            raise NotImplementedError

        def move_up(self):
            raise NotImplementedError

        def move_down(self):
            raise NotImplementedError

        def has_moves(self):
            raise NotImplementedError

        def get_score(self):
            raise NotImplementedError

matrix = [[0 for x in range(4)]for y in range(4)]

def draw_field(stdscr):
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    height, width = stdscr.getmaxyx()

    curses.curs_set(False)
    title = "2048"
    statusbarstr = "Press 'q' to exit"

    # Render status bar
    stdscr.addstr(height-1, 0, statusbarstr)
    stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))

    # Render title
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(1, width//2 - len(title)//2, title)

    # Render field
    field = curses.newpad(9, 29) 

    for x in range(0, 21, 5):
        for sy in range(1, 8, 2):
            field.addstr(sy, x,u'\u2502')

    for y in range(0, 10, 2):
        if y == 0:
            field.addstr(0, 0, u'\u250C' + (u'\u252C').join([u'\u2500' * 4]*4) + u'\u2510')
        elif y == 8:
            field.addstr(8, 0, u'\u2514' + (u'\u2534').join([u'\u2500' * 4]*4) + u'\u2518')
        else:   
            field.addstr(y, 0, u'\u251C' + (u'\u253C').join([u'\u2500' * 4]*4) + u'\u2524')
    
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            field.addstr(1 + 2*y, 1 + 5*x, str(value if value else '').center(4))


    field.refresh(0, 0, 5,40, 14, 69)
    stdscr.refresh()

    running = True
    while  running:
        k = stdscr.getch()

        if k == ord('q') or k == 27:
            running = False
            break


def main():
    curses.wrapper(draw_field)

if __name__ == "__main__":
    main()