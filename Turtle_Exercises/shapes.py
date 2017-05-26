from turtle import *

def circle():
    circle(50)


def star(size):
    for i in range(5):
        forward(size)
        right(144)


def square():
    for i in range(4):
        forward(50)
        right(90)


def pentagon():
    for i in range(5):
        forward(200)
        right(72)


def octagon():
    for i in range(8):
        forward(100)
        right(45)


def hexagon():
    for i in range(6):
        forward(100)
        right(60)


def triangle():
    for i in range(3):
        forward(175)
        right(120)

def diamond():
    for i in range(2):
        forward(100)
        right(110)
        forward(75)
        right(70)

def full_star(size):

    for side in range(5):
        forward(size)
        left(36)
        forward(size)
        right(108)
