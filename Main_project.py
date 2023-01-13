import turtle



screen = turtle.Screen()

reticle = "Reticle.gif"

screen.addshape(reticle)
turtle.shape(reticle)

screen.bgcolor("black")

from turtle import numinput

distance = numinput("Distance", "range in meters:", 300, minval=50, maxval=1000)


turtle.mainloop()
