import turtle

turtle.pensize(2)
turtle.pencolor('black')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()


def keke_line(n=3, len=360):
    if n == 0:
        turtle.fd(len)
    else:
        for i in [0, 60, -120, 60]:
            turtle.left(i)
            keke_line(n - 1, len / 3)


keke_line()

turtle.hideturtle()
turtle.done()
