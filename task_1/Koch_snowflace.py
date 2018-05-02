import turtle

lenght = 300
a = [0, 0]
b = [lenght, 0]
c = [lenght/2, -((3*0.5)/2)*lenght]

def draw_triangle(a, b, c):
	turtle.up()
	turtle.goto(a)
	turtle.down()
	turtle.goto(b)
	turtle.goto(c)
	turtle.goto(a)

draw_triangle(a, b, c)