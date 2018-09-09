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


#initiating player speed
playerspeed = 15


#choose number of enemy
numenemy = 5

#create empty list
enemyarray = []


#add enemies to the array creating mutlitple enemies
for i in range(numenemy):
    enemyarray.append(turtle.Turtle())


#creating attributes and position for enemies
for enemy in enemyarray:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


#initiating enemy speed
enemyspeed = 2



#create bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()


#initiating bullet speed
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

    for enemy in enemyarray:
        #move enemy alternating xcor
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #reverse if enemy hits border
        if enemy.xcor() > 280:
            #move all enemies across
            for e in enemyarray:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #move all enemies down
            for e in enemyarray:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemies direction
            enemyspeed *= -1

        #checking collion between bullet and enemy
        if collision(bullet,enemy):
            #reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

        #checking collision between player and enemy
        if collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            break
            print("Gamer Over")

    #move bullet if its in fire state
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #bordercheck for bullet
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    








