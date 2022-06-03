import turtle

a = 0
b = 0
turtle.bgcolor("black")
turtle.speed(20)
turtle.pencolor("green")
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
while True:
    turtle.forward(a)
    turtle.right(b)
    a += 3
    b += 1
    if b == 200:
        break


#turtle.bgcolor("black")
#turtle.pensize(3)
#turtle.speed(20)
#for i in range(6):
#    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
#        turtle.color(colours)
#        turtle.circle(100)
#        turtle.left(10)
#turtle.hideturtle()
turtle.exitonclick()