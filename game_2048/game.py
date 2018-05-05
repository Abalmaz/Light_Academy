import curses

def draw_field(field):
    for x in range(0, 21, 5):
        for sy in range(1, 8, 2):
            field.addstr(sy, x,'\u2502')

    for y in range(0, 10, 2):
        if y == 0:
            field.addstr(0, 0, '\u250C' + ('\u252C').join(['\u2500' * 4]*4) + '\u2510')
        elif y == 8:
            field.addstr(8, 0, '\u2514' + ('\u2534').join(['\u2500' * 4]*4) + '\u2518')
        else:   
            field.addstr(y, 0, '\u251C' + ('\u253C').join(['\u2500' * 4]*4) + '\u2524')


class Game:

    def __init__(self):
        self.screen = curses.initscr()
   
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

    def get_field(self):
        curses.start_color()
        curses.curs_set(False)

        self.screen.clear()
        self.screen.refresh()

        # Start colors in curses
        curses.start_color()
        height, width = self.screen.getmaxyx()

        curses.curs_set(False)
        title = "2048"
        statusbarstr = "Press 'q' to exit"

        # Render status bar
        self.screen.addstr(height-1, 0, statusbarstr)
        self.screen.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))

        # Render title
        self.screen.attron(curses.A_BOLD)
        self.screen.addstr(1, width//2 - len(title)//2, title)
        field = curses.newpad(9, 29)
        draw_field(field)

        field.refresh(0, 0, 5,40, 14, 69)
        self.screen.refresh()

def main():
    game = Game()
    field = game.get_field()

    running = True

    while running:
        k = game.screen.getch()
        if k == ord('q'):
            running == False
            break

        # cell_width = len(str(max(
        #     cell
        #     for row in field
        #     for cell in row
        # )))

        # print("\033[H\033[J", end="")
        # print("Score: ", game.get_score())
        # print('\n'.join(
        #     ' '.join(
        #         str(cell).rjust(cell_width)
        #         for cell in row
        #     )
        #     for row in field
        # ))

        # if not game.has_moves():
        #     print("No available moves left, game over.")
        #     break

        # print("L, R, U, D - move")
        # print("Q - exit")

        # try:
        #     c = input("> ")
        # except (EOFError, KeyboardInterrupt):
        #     break

        # if c in ('l', 'L'):
        #     game.move_left()
        # elif c in ('r', 'R'):
        #     game.move_right()
        # elif c in ('u', 'U'):
        #     game.move_up()
        # elif c in ('d', 'D'):
        #     game.move_down()
        # elif c in ('q', 'Q'):
        #     break

    #print("Bye!")


if __name__ ==  '__main__':
    curses.wrapper(main())
