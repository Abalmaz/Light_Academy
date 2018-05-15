import random

matrix = [[0 for x in range(4)]for y in range(4)]

#matrix = [[2, 4, 0, 0]]

def get_empty_cell(matrix):
        empty = []
        for y, row in enumerate(matrix):
            for x, value in enumerate(row):
                if value == 0:
                    empty.append([y, x])
        return empty
        
def add_number(matrix):
    empty_cells = get_empty_cell(matrix)
    if empty_cells:
        number = 2 if random.random() < 0.9 else 4
        random_cell = empty_cells[random.randrange(0, len(empty_cells))]
        matrix[random_cell[0]][random_cell[1]] = number

add_number(matrix)
add_number(matrix)
add_number(matrix)
add_number(matrix)
add_number(matrix)
add_number(matrix)
add_number(matrix)
add_number(matrix)
add_number(matrix)

print(matrix)

def move_zero(matrix):
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if row[x] == 0:
                row.insert(0, row.pop(x))
    return matrix            	

def move_right(matrix):
    new_matrix = move_zero(matrix)
    print(new_matrix)
    for y, row in enumerate(new_matrix):
        for x, value in enumerate(reversed(row)):
            print(x, value)    
            if row[x] != 0 and x<3:
                if row[x] == row[x+1]:
                    row[x], row[x+1] = 0, row[x]*2
                elif row[x] > row[x+1]:
                    row[x], row[x+1] = row[x+1], row[x]
           
    #move_zero(new_matrix)                	
    return new_matrix        			
        		
def move_left(matrix):
    for row in matrix:
        row.reverse()
    move_right(matrix)    
    for row in matrix:
        row.reverse()

#move_left(matrix)
#move_zero(matrix)
move_right(matrix)
print(matrix)            