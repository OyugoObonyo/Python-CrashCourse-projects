"""
Using the tutle module to draw a square
"""
import random
from turtle import Turtle, Screen
import turtle

turtle.colormode(255)
t = Turtle()
t.speed("fastest")


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_spirograph():
    r = 50
    for i in range(360):
        t.color(random_colour())
        t.circle(r)
        t.right(i)


draw_spirograph(100)

s = Screen()
s.exitonclick()
