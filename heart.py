import turtle

turtle.bgcolor("black")
turtle.pensize(5)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("red", "red")

turtle.begin_fill()
turtle.left(130)
turtle.forward(171.65)
curve()

turtle.left(148)
curve()
turtle.forward(171.65)
turtle.hideturtle()
turtle.end_fill()

turtle.done()