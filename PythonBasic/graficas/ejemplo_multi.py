
import turtle

a = 0
b = 0
c=0

turtle.bgcolor("black")
turtle.speed(5)
turtle.pencolor("green")
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.tilt(30)


while True:
     turtle.forward(a)
     turtle.right(b)
     turtle.left(c)
     a += 3
     b += 1
     c += -1
     if b == 200:
          break
turtle.exitonclick()