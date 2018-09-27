# coding: utf-8
# imports

import turtle
import random
import math

import first


PHI = 360 / 7
RADIUS = 50


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(color, rad):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()


def draw_pistol(base_x, base_y):
    # обойма
    gotoxy(base_x, base_y)
    draw_circle('grey', 80)
    # мушка
    gotoxy(base_x, base_y + 160)
    draw_circle('red', 3)
    # барабан
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180
        gotoxy(math.sin(phi_rad) * RADIUS + base_x, math.cos(phi_rad) * RADIUS + base_y + 60)
        draw_circle('white', 22)


def anim_pistol(base_x, base_y, start):
    for i in range(start, random.randrange(7, 100)):
        phi_rad = PHI * i * math.pi / 180
        gotoxy(math.sin(phi_rad) * RADIUS + base_x, math.cos(phi_rad) * RADIUS + base_y + 60)
        draw_circle('black', 22)
        draw_circle('white', 22)
    gotoxy(math.sin(phi_rad) * RADIUS + base_x, math.cos(phi_rad) * RADIUS + base_y + 60)
    draw_circle('black', 22)
    return i % 7


##########################

turtle.speed(0)

x_pos = 0 # int(turtle.textinput("Position", "Укажите позицию Х"))
y_pos = 0 # int(turtle.textinput("Position", "Укажите позицию У"))

draw_pistol(x_pos, y_pos)

start = 0
answer = ''
while answer != 'n':
    answer = turtle.textinput("Answer", "Поиграем? (y/n)")
    if answer == 'y':
        start = anim_pistol(x_pos, y_pos, start)

        if start == 0:
            gotoxy(-150, 250)
            turtle.write("БА-БАХ!!!", font=("Arial", 22, "bold"))
            
    else:
        pass
