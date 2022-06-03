import turtle
sc = turtle.Screen()
sc.setup(600, 600)
spiral = turtle.Turtle()
spiral.speed(10)
sc.bgcolor("black")
col=("yellow", "orange", "red", "orange", "yellow")
c = 0
#def new_func(spiral):
   # spiral.fillcolor('violet')
    #col= turtle.pencolor()
    #spiral.fillcolor(col)
    #spiral.fillcolor(0, .5, 3)
    #return col

#col = new_func(spiral)
for i in range(10):
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(col[c])
    if c == 3:
        c = 0
    else:
        c += 1
