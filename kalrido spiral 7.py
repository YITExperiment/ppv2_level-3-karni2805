import turtle

from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple','pink','white'])


def draw_circle(size):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    draw_circle(size+5)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(5)
draw_circle(30)
