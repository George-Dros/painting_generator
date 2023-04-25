import turtle as t
from colors import color_list
import random

def paint():
    for dot in range(0, 10):
        art.color(random.choice(color_list))
        art.pendown()
        art.circle(2)
        art.penup()
        art.forward(50)



art = t.Turtle()
art.hideturtle()
art.speed("fastest")
t.colormode(255)
art.penup()
art.width(20)
art.setx(-200)
art.sety(-200)

for row in range(0,10):
    paint()
    art.penup()
    art.setx(-200)
    art.sety(-200 + (row+1)*50)


screen = t.Screen()
screen.exitonclick()

