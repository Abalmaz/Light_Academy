from math import log
import curses
from game import Game

class Renderer:
    COLOR_THEME = [
        # (foreground, background)
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

    COLOR_256 = [
        (7, 0),
        (6, 0),
        (4, 0),
        (5, 0),
        (1, 0),
        (3, 0),
        (2, 0),
        (6, 7),
        (4, 7),
        (5, 7),
        (1, 7),
    ]    

    def __init__(self, game, stdscr=None):
        self.stdscr = stdscr
        self.game = game
        self.field = curses.newpad(9, 29)


    def draw_field(self):
        # Clear and refresh the screen for a blank canvas
        self.stdscr.clear()
        self.stdscr.refresh()

        # Start colors in curses
        curses.start_color()

        if curses.has_colors():
            if curses.COLORS != 256:
                color = Renderer.COLOR_THEME
            else:
                color = Renderer.COLOR_256    

            for i, color_pair in enumerate(color, 1):
                curses.init_pair(i, *color_pair)

        height, width = self.stdscr.getmaxyx()

        curses.curs_set(False)
        title = "2048"
        statusbarstr = "Press 'q' to exit"

        # Render status bar
        self.stdscr.addstr(height-1, 0, statusbarstr)
        self.stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))

        # Render title
        self.stdscr.attron(curses.A_BOLD)
        self.stdscr.addstr(1, width//2 - len(title)//2, title)

        self.stdscr.addstr(4, 0, "Moves: %i" % (self.game.moves), curses.A_BOLD)
        self.stdscr.addstr(6, 0, "Score: %i" % (self.game.score), curses.A_BOLD)        
        self.stdscr.keypad(True)

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
                self.field.addstr(1 + 2*y, 1 + 5*x, str(value if value else '').center(4), curses.color_pair(int(log(value,2)) if value else 1))

        self.field.refresh(0, 0, 8, 1, 20, 40)
        self.stdscr.refresh()

  
    def get_key(self):
        while  True:
            
            k = self.stdscr.getch()

            if k == ord('q') or k == 27:
                curses.endwin()
                exit()
                break
                                            
            if k == ord('w'):
                self.game.move_up()
                self.game.add_number()
                break
        
            if k == ord('s'):
                self.game.move_down()
                self.game.add_number()
                break
        
            if k == ord('a'):
                self.game.move_left()
                self.game.add_number()
                break
            
            if k == ord('d'):
                self.game.move_right()
                self.game.add_number()
                break

    def game_over(self):
        # height, width = self.stdscr.getmaxyx()        
        # self.stdscr.addstr(4, 0, 'You lost!'.center(width) )
        curses.endwin()
        print("You lose!")
        print("Your score was %s" % self.game.score)
        exit(0)

    def render(self):
        while self.game.has_moves():
            self.draw_field()
            self.get_key()
        self.game_over()        


                                                        

def draw_game(stdscr):
    game = Game()
    game.add_number()
    game.add_number()
    render = Renderer(game, stdscr)
    render.render()

def main():
    curses.wrapper(draw_game)

if __name__ == "__main__":
    main()