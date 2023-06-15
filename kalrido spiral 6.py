import turtle

from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple','pink','white'])


def draw_circle(size,angle,shift,shape):
    turtle.bgcolor('black')
    turtle.pencolor(next(colors))
    if shape =='circle':
        turtle.circle(size)
        next_shape = 'square'
    elif shape =='square':
        for i in range(4):
            turtle.forward(size +2)
            turtle.left(90)
        next_shape = 'circle'
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5, angle+1,shift+1,next_shape)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30,0,1,'circle')
