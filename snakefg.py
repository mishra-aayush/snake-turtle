# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:34:14 2020
Snake game using the turtle module

@author: AAYUSH MISHRA
"""

from random import *
import turtle as t
from freegames import square, vector

t.title("Snake")
root  = t.Screen()._root
t.bgcolor('#111111')

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    head = snake[-1].copy()
    if len(snake) > 1:
        headnext = snake[-2].copy()
        if head.x-headnext.x > 0 and aim.x < 0:
            aim.x = 10
        elif head.x-headnext.x < 0 and aim.x > 0:
            aim.x = -10
        elif head.y-headnext.y > 0 and aim.y < 0:
            aim.y = 10
        elif head.y-headnext.y < 0 and aim.y > 0:
            aim.y = -10
            
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, '#FFDC00')
        square(0, 0, 9, '#111111')
        t.update()
        t.color('white')
        style = ('Arial', 30, 'bold')
        t.write('Score: '+ str(len(snake)-1), font=style, align='center')
        return

    snake.append(head)

    if head == food:
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    t.clear()

    for body in snake:
        square(body.x, body.y, 9, '#c7291e')

    square(food.x, food.y, 9, '#2ECC40')
    t.update()
    t.ontimer(move, 100)

t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
t.listen()
t.onkey(lambda: change(10, 0), 'Right')
t.onkey(lambda: change(-10, 0), 'Left')
t.onkey(lambda: change(0, 10), 'Up')
t.onkey(lambda: change(0, -10), 'Down')
move()
t.done()