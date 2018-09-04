import sys
import os
import random
import turtle
import math

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


#choose number of enemy
numenemy = 5
#create empty list
enemyarray = []


#add enemies to the 
for i in range(numenemy):
    enemyarray.append(turtle.Turtle())

#creating enemy
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

bulletstate = "ready"


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

#function fire bullet
def firebullet():
    #declare global state easy to edit
    global bulletstate


    if bulletstate == "ready":
        #change state to fire
        bulletstate = "fire"
        #set bulletposition
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


#collision detection
def collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

    
#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(firebullet, "space")

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

    #move bullet if its in fire state
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #bordercheck for bullet
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    #checking collion between bullet and enemy
    if collision(bullet,enemy):
        #reset bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        #reset enemy
        enemy.setposition(-200,250)

    #checking collision between player and enemy
    player.hideturtle()
    enemy.hideturtle()
    print("Gamer Over")
    break








