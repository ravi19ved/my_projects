import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

alex.color("red")

alex.forward(50)
alex.left(90)
alex.forward(30)



wn.bgcolor("lightgreen")
wn.title("Hello Tess!")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

tess.forward(50)
tess.left(120)
tess.forward(50)


wn.mainloop()