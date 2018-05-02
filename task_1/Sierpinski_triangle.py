import turtle

lenght = 300
a = [0, 0]
b = [lenght, 0]
c = [lenght/2, ((3*0.5)/2)*lenght]


def middle_point(a, b):
	x = (a[0] + b[0])/2
	y = (a[1] + b[1])/2
	point = [x, y]
	return point


def sierpinski (a, b, c, n):
	mid_a = middle_point(a, b)
	mid_b = middle_point(b, c)
	mid_c = middle_point(a, c)
	turtle.up()
	turtle.goto(mid_c)
	turtle.down()
	turtle.goto(mid_b)
	turtle.goto(mid_a)
	turtle.goto(mid_c)
	if n > 0 :
	    sierpinski(c, mid_c, mid_b, n-1)
	    sierpinski(b, mid_a, mid_b, n-1)
	    sierpinski(a, mid_c, mid_a, n-1)
	

def draw_triangle(a, b, c):
	turtle.up()
	turtle.goto(a)
	turtle.down()
	turtle.goto(b)
	turtle.goto(c)
	turtle.goto(a)

draw_triangle(a, b, c)
sierpinski(a, b, c, 5)
