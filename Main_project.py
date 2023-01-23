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

distance = numinput("Distance", "range in yards: (0-1000)", 100, minval=0, maxval=1000)

def Change_In_Reticle(distance):
    if distance == 0:
        adjust = -1.5
    elif distance <= 25:
        adjust = -0.64
    elif distance <= 50:
        adjust = -1
    elif distance <= 75:
        adjust = -0.11
    elif distance <= 100:
        adjust = -0
    elif distance <= 125:
        adjust = -0.45
    elif distance <= 150:
        adjust = -1.27
    elif distance <= 175:
        adjust = -2.45
    elif distance <= 200:
        adjust = -4.02
    elif distance <= 225:
        adjust = -5.99
    elif distance <= 250:
        adjust = -8.37
    elif distance <= 275:
        adjust = -11.18
    elif distance <= 300:
        adjust = -14.44
    elif distance <= 325:
        adjust = -18.16
    elif distance <= 350:
        adjust = -22.37
    elif distance <= 375:
        adjust = -27.08
    elif distance <= 400:
        adjust = -32.31
    elif distance <= 425:
        adjust = -38.09
    elif distance <= 450:
        adjust = -44.44
    elif distance <= 475:
        adjust = -51.37
    elif distance <= 500:
        adjust = -58.93
    elif distance <= 525:
        adjust = -67.12
    elif distance <= 550:
        adjust = -75.98
    elif distance <= 575:
        adjust = -85.54
    elif distance <= 600:
        adjust = -95.83
    elif distance <= 625:
        adjust = -106.87
    elif distance <= 650:
        adjust = -118.71
    elif distance <= 675:
        adjust = -131.37
    elif distance <= 700:
        adjust = -144.90
    elif distance <= 725:
        adjust = -159.32
    elif distance <= 750:
        adjust = -174.68
    elif distance <= 775:
        adjust = -191.02
    elif distance <= 800:
        adjust = -208.39
    elif distance <= 825:
        adjust = -226.82
    elif distance <= 850:
        adjust = -246.36
    elif distance <= 875:
        adjust = -267.06
    elif distance <= 900:
        adjust = -288.97
    elif distance <= 925:
        adjust = -312.14
    elif distance <= 950:
        adjust = -336.62
    elif distance <= 975:
        adjust = -362.47
    elif distance <= 1000:
        adjust = -389.74
    return adjust

Draw_Reticle(Reticle, 0, Change_In_Reticle(distance))
turtle.mainloop()
