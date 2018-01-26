import turtle
from random import randint
# the distance we want the pointer to travel each time
totalmoves = randint(0, 100)

colors = ["red", "green", "blue", "orange"]

for j in range(0, totalmoves):
    turtle.right(j)
    turtle.forward(15)
    for k in colors:
        turtle.color(k)
