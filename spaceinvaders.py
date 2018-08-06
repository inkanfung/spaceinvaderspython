import sys
import os
import random
import turtle

#setting up screen
wn = turtle.Screen()
wn.bgcolour("black")
wn.title("Space Invaders")

#draw border
border = turtle.Turtle()
border.speed(0)
border.color("white")

#setting up position
border.penup()
border.setposition(-50,-50)
border.pendown()
border.pensize(3)

#drawing square
for side in range(4):
    border.fd(50)
    border.lt(5)
border.hideturtle()

#create the player turtle
player = turtle.Turtle()
player.color("red")
player.shape("circle")
player.penup()
player.speed(0)
player.setposition(0, -20)
player.sethead(90)
