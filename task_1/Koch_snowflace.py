import math
from turtle import Turtle, Screen

snowflace = Turtle()
screen = Screen()
#screen.tracer(0)
#screen.delay(1000)
tr_length = 300

def draw_triangle(tr_length):
	triangle = []
	for i in range(3):
		point_i = snowflace.pos()
		triangle.append(point_i)
		snowflace.left(120)
		snowflace.forward(tr_length)
	return triangle


def coord_part_of_line(first_point, second_point, part):
	coord_x = (first_point[0] + part*second_point[0])/(1+part)
	coord_y = (first_point[1] + part*second_point[1])/(1+part)
	point = [coord_x, coord_y]
	return point

def coord_third_point(a, b, axis):
	if axis == 'x':
		return (b[0]-a[0])*math.cos(60)-(b[1]-a[1])*math.sin(60)+a[0]
	elif axis == 'y':
		return (b[0]-a[0])*math.sin(60)+(b[1]-a[1])*math.cos(60)+a[1]
	else:
		return 1		

def length_line_between_point(first_point, second_point):
	return ((second_point[0] - first_point[0])**2 + (second_point[1] - first_point[1])**2)*0.5	

def koch(a, b, n):
	left_point = coord_part_of_line(a, b, 1/2)
	right_point = coord_part_of_line(a, b, 2)
	center_point = []
	
	length_line = length_line_between_point(left_point, right_point)

	center_point.append(coord_third_point(left_point, right_point, 'x'))
	center_point.append(coord_third_point(left_point, right_point, 'y'))

	snowflace.up()
	snowflace.goto(left_point)
	snowflace.color('white')
	snowflace.down()
	snowflace.goto(right_point)
	snowflace.color('black')
	snowflace.goto(center_point)
	snowflace.goto(left_point)


triangle = draw_triangle(tr_length)
#screen.update()
point_a = triangle[0]
point_b = triangle[1]
point_c = triangle[2]


#snowflace.reset()
koch(point_a, point_b, 1)

#draw_edges(point_b, point_c, 60, 1)

#screen.update()
#snowflace.reset()
#turtle.reset()
#turtle.hideturtle() 

screen.exitonclick()
