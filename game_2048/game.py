import curses
class Game:
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
        stdscr = curses.initscr()

        #Properly initialize the screen
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

        #Check and begin color support
        if curses.has_colors():
        	curses.start_color()

        stdscr.addstr(curses.LINES-1, 0, "Press 'Q' ro quit")
        game_window = curses.newwin(curses.LENES-2, curses.COLS, 1, 0)

        while True:

        	c = quote_window.getch()
        		
        	if c == ord('q') or c == ord('Q'):
        		break	


def main():
    game = Game()

    while True:
        field = game.get_field()
        cell_width = len(str(max(
            cell
            for row in field
            for cell in row
        )))

        print("\033[H\033[J", end="")
        print("Score: ", game.get_score())
        print('\n'.join(
            ' '.join(
                str(cell).rjust(cell_width)
                for cell in row
            )
            for row in field
        ))

        if not game.has_moves():
            print("No available moves left, game over.")
            break

        print("L, R, U, D - move")
        print("Q - exit")

        try:
            c = input("> ")
        except (EOFError, KeyboardInterrupt):
            break

        if c in ('l', 'L'):
            game.move_left()
        elif c in ('r', 'R'):
            game.move_right()
        elif c in ('u', 'U'):
            game.move_up()
        elif c in ('d', 'D'):
            game.move_down()
        elif c in ('q', 'Q'):
            break

    print("Bye!")


if __name__ ==  '__main__':
    main()
