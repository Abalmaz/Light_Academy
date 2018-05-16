import curses
import random

class Game:
    def __init__(self):
        self.matrix = [[0 for x in range(4)]for y in range(4)]
        self.score = 0
        self.moves = 0

    def get_empty_cell(self):
        empty = []
        for y, row in enumerate(self.matrix):
            for x, value in enumerate(row):
                if value == 0:
                    empty.append([y, x])
        return empty
        
    def add_number(self):
        empty_cells = self.get_empty_cell()
        if empty_cells:
            number = 2 if random.random() < 0.9 else 4
            random_cell = empty_cells[random.randrange(0, len(empty_cells))]
            self.matrix[random_cell[0]][random_cell[1]] = number
        return self.matrix    

    def move_zero(self):
        for y, row in enumerate(self.matrix):
            for x in range(3, -1, -1):
                if row[x] == 0:
                    row.append(row.pop(x))
        return self.matrix                         
   

    def revers_matrix(self, matrix):
        new_matrix = [[value for x, value in enumerate(reversed(row))] for row in matrix]
        return new_matrix

    def transponse_matrix(self, matrix):
        trans_matrix = [list(i) for i in zip(*matrix)]
        return trans_matrix              
                        

    def move_left(self, matrix = None):
        self.move_zero()
        for row in self.matrix:
            for x in range(4):
                if x<3 and row[x] == row[x+1]:
                    row[x], row[x+1] = row[x]*2, 0
                    self.score += row[x]*2
        self.move_zero()
        self.moves += 1
        return self.matrix

    def move_right(self):
        self.matrix = self.revers_matrix(self.matrix)       
        self.move_left()
        self.matrix = self.revers_matrix(self.matrix)
        return self.matrix

    def move_up(self):
        self.matrix = self.transponse_matrix(self.matrix)
        self.move_left()
        self.matrix = self.transponse_matrix(self.matrix)
        return self.matrix

    def move_down(self):
        self.matrix = self.transponse_matrix(self.matrix)
        self.move_right()
        self.matrix = self.transponse_matrix(self.matrix)
        return self.matrix
     

    def has_moves(self):
        if self.get_empty_cell():
            return True
          

    def get_score(self):
        return self.score

game = Game()

game.add_number()


print('add number')
for y, row in enumerate(game.matrix):
    for x, value in enumerate(row):
        print(value, end = ' ')
    print()

game.move_left()
print('move left')
for y, row in enumerate(game.matrix):
    for x, value in enumerate(row):
        print(value, end = ' ')
    print()

game.move_right()
print('move right')
for y, row in enumerate(game.matrix):
    for x, value in enumerate(row):
        print(value, end = ' ')
    print()

game.move_up()
print('move up')
for y, row in enumerate(game.matrix):
    for x, value in enumerate(row):
        print(value, end = ' ')
    print()         

game.move_down()
print('move down')
for y, row in enumerate(game.matrix):
    for x, value in enumerate(row):
        print(value, end = ' ')
    print()  

  

