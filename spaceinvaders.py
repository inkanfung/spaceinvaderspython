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
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)


playerspeed = 15


#creating enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("square")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)


enemyspeed = 2


#create bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

#defining the bullet states
#ready to fire state
#fire state 


#moving player left and right

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x >280:
        x = 280
    player.setx(x)
    
#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

#main gameloop
while True:

    #move enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #reverse if enemy hits border
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 20
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 20
        enemyspeed *= -1
        enemy.sety(y)












