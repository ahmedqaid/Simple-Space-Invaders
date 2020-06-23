import math
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders by QQ")
wn.screensize(600, 600)
wn.tracer(2)

player = turtle.Turtle()
player.speed(0)
player.penup()
player.setposition(0, -250)
player.color("red")
player.left(90)
player.shapesize(4)

sc = 0
score = turtle.Turtle()
score.hideturtle()
score.color("white")
score.setposition(-350, 280)
score.write(sc, move=False, align="left", font=("segeo ui", 20, "normal"))

fireball = turtle.Turtle()
fireball.hideturtle()
fireball.speed(0)
fireball.penup()
fireball.shape("circle")
fireball.color("yellow")
fireball.left(90)

maxenemy = 8
enemy = []

for x in range(maxenemy):
    enemy.append(turtle.Turtle())
    enemy[x].penup()
    enemy[x].speed(0)
    enemy[x].shape("triangle")
    enemy[x].color("green")
    if x == 0 :
        a = -225
        b = 250
    elif x == 1 :
        a = -75
        b = 250
    elif x == 2 :
        a = 75
        b = 250
    elif x == 3 :
        a = 225
        b = 250
    elif x == 4 :
        a = -225
        b = 150
    elif x == 5 :
        a = -75
        b = 150
    elif x == 6 :
        a = 75
        b = 150
    elif x == 7 :
        a = 225
        b = 150
    enemy[x].setposition(a, b)


def keepmovin():
    if enemy[3].xcor() > 290:
        for y in range(maxenemy):
            enemy[y].left(180)

    if enemy[0].xcor() < -290:
        for y in range(maxenemy):
            enemy[y].left(180)

    for x in range(maxenemy):
        enemy[x].forward(1)

def goleft():
    x = player.xcor() - 30
    y = player.ycor()
    player.setposition(x, y)

def goright():
    x = player.xcor() + 30
    y = player.ycor()
    player.setposition(x, y)

def collision():
    global sc
    for i in range(maxenemy):
        d = math.sqrt(math.pow(fireball.xcor() - enemy[i].xcor(), 2) + math.pow(fireball.ycor() - enemy[i].ycor(), 2))
        if d < 20:
            if not enemy[i].isvisible():
                return
            sc += 10
            score.clear()
            score.write(sc, move=False, align="left", font=("segeo ui", 20, "normal"))
            fireball.hideturtle()
            fireball.forward(0)
            enemy[i].hideturtle()

def fire():
    fireball.setposition(player.xcor(), player.ycor() + 5)
    fireball.showturtle()
    x = 0
    while (x < 70):
        keepmovin()
        fireball.forward(10)
        collision()
        x += 1


turtle.listen()
turtle.onkey(goleft ,"Left")
turtle.onkey(goright ,"Right")
turtle.onkey(fire ,"space")

while (True):
    keepmovin()
    if sc == 80:
        score.clear()
        score.write("Game Over", move=False, align="left", font=("segeo ui", 20, "normal"))

#Fixed: Counting score
#Fix: frame rate
#Add AI
