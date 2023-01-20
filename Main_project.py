import turtle



screen = turtle.Screen()

#reticle = "Reticle.gif"

#screen.addshape(reticle)
#turtle.shape(reticle)

screen.bgpic("Background2.gif")

Reticle = turtle.Turtle()

def Draw_Reticle(Reticle, x, y):

    Reticle.hideturtle()

    Reticle.penup()
    Reticle.goto(x,y)
    Reticle.pendown()

    Reticle.dot(10, "red")

    Reticle.penup()
    Reticle.goto(x, y-30)
    Reticle.pendown()
    Reticle.pencolor("red")
    Reticle.width(3)
    Reticle.circle(30)


from turtle import numinput

distance = numinput("Distance", "range in meters: (50-1000)", 300, minval=50, maxval=1000)

def Change_In_Reticle(distance):
    adjust = (distance - 300) / -50
    return adjust

Draw_Reticle(Reticle, 0, Change_In_Reticle(distance) * 10)
turtle.mainloop()
