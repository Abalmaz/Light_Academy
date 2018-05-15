import curses
from game import Game

class Renderer:
    def __init__(self, game):
        self.stdscr = curses.initscr()
        self.game = game
        self.field = curses.newpad(9, 29)

    def draw_table(self, stdscr):
        # Clear and refresh the screen for a blank canvas
        self.stdscr.clear()
        self.stdscr.refresh()

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

        for x in range(0, 21, 5):
            for sy in range(1, 8, 2):
                self.field.addstr(sy, x,u'\u2502')

        for y in range(0, 10, 2):
            if y == 0:
                self.field.addstr(0, 0, u'\u250C' + (u'\u252C').join([u'\u2500' * 4]*4) + u'\u2510')
            elif y == 8:
                self.field.addstr(8, 0, u'\u2514' + (u'\u2534').join([u'\u2500' * 4]*4) + u'\u2518')
            else:   
                self.field.addstr(y, 0, u'\u251C' + (u'\u253C').join([u'\u2500' * 4]*4) + u'\u2524')      

        for y, row in enumerate(self.game.matrix):
            for x, value in enumerate(row):
                self.field.addstr(1 + 2*y, 1 + 5*x, str(value if value else '').center(4))

        self.field.refresh(0, 0, 5,40, 14, 69)
        self.stdscr.refresh()

        running = True
        while  running:
            k = self.stdscr.getch()

            if k == ord('q') or k == 27:
                running = False
                break        

def main():
    game = Game()
    game.add_number()
    game.add_number()
    renderer = Renderer(game)
    curses.wrapper(renderer.draw_table)
    # game.add_number()
    # game.add_number()
    #curses.wrapper(renderer.draw_table)

if __name__ == "__main__":
    main()