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
   

    def revers_matrix(self):
        new_matrix = [[value for x, value in enumerate(reversed(row))] for row in self.matrix]
        return new_matrix

    def tranponse_matrix(self):
        trans_matrix = [list(i) for i in zip(*self.matrix)]
        return trans_matrix              
                        

    def move_left(self):
        move_zero(self.matrix)
        for row in self.matrix:
            for x in range(4):
                if x<3 and row[x] == row[x+1]:
                    row[x], row[x+1] = row[x]*2, 0
                    self.score += row[x]*2
        move_zero(self.matrix)
        self.moves += 1
        return self.matrix

    def move_right(self):
        reversed_matrix = revers_matrix(self.matrix)
        move_left(reversed_matrix)
        self.matrix = revers_matrix(reversed_matrix)
        return self.matrix

    def move_up(self):
        tr_matrix = tranponse_matrix(self.matrix)
        move_left(tr_matrix)
        self.matrix = tranponse_matrix(tr_matrix)
        return self.matrix

    def move_down(self):
        tr_matrix = tranponse_matrix(self.matrix)
        tr_matrix = move_right(tr_matrix)
        self.matrix = tranponse_matrix(tr_matrix)
        return self.matrix
     

    def has_moves(self):
        if get_empty_cell(self):
            return True

    def get_score(self):
        return self.score
          

