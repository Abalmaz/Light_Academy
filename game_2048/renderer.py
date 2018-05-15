import curses
import game

class Renderer:
    def __init__(self):
        self.stdscr = curses.initscr()
        self.field = curses.newpad(9, 29)

    def draw_table(self):

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

    def start(self):

        for y, row in enumerate(game.matrix):
            for x, value in enumerate(row):
                self.field.addstr(1 + 2*y, 1 + 5*x, str(value if value else '').center(4))
		            

def main(_):
    renderer = Renderer()
    # game.add_number()
    # game.add_number()
    renderer.draw_table()

if __name__ == "__main__":
    curses.wrapper(main)