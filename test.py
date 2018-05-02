import turtle

lenght = 160
x = 0
y = 0 

def draw_triangle(x, y, lenght):
	turtle.goto(x, y)
	for i in range(3):	
		turtle.forward(lenght)
		turtle.left(120)

draw_triangle(x, y, lenght)		

