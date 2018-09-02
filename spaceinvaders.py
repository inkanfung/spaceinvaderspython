import sys
import os
import random
import turtle

#setting up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#draw border
border = turtle.Turtle()
border.speed(0)
border.color("white")

#setting up position
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)

#drawing square
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

#create the player turtle
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
