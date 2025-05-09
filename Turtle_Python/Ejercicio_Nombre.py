import turtle 


turtle.bgcolor("black")  


turtle.speed(10)
turtle.pensize(10)

def curveMove():
  for i in range(200):
    turtle.rt(1)
    turtle.fd(1)

t = turtle.Turtle()
t.speed(3)
t.shape("circle")
t.pensize(35)

# S
t.color("white")
t.penup()
t.goto(-490, -90)
t.setheading(0)
t.pendown()
t.rt(20)
t.circle(40, 180)
t.circle(-40, 180)

# T
t.color("white")
t.penup()
t.goto(-330, -90)
t.setheading(90)
t.pendown()
t.fd(140)
t.rt(90)
t.bk(45)
t.fd(90)

# I
t.color("white")
t.penup()
t.goto(-200, -90)
t.setheading(90)
t.pendown()
t.fd(140)

# V 
t.color("white")
t.penup()
t.goto(-70, -90)
t.setheading(90)
t.pendown()
t.rt(25)
t.fd(150)
t.bk(150)
t.lt(50)
t.fd(150)t.rt(-200)


# E
t.color("white")
t.penup()
t.goto(60, 50)
t.setheading(270)
t.pendown()
t.fd(140)
t.bk(140)
t.setheading(0)
t.fd(80)
t.penup()
t.goto(60, -20)
t.setheading(0)
t.pendown()
t.fd(70)
t.penup()
t.goto(60, -90)
t.setheading(0)
t.pendown()
t.fd(80)

# N
t.color("white")
t.penup()
t.goto(220, -90)
t.setheading(90)
t.pendown()
t.fd(140)
t.rt(145)
t.fd(170)
t.lt(145)
t.fd(140)


turtle.done()
