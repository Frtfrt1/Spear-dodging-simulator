import turtle
import random

def up():
     ae = ["cyan", "firebrick", "violet", "gold", "silver", "aquamarine", "lime", "green", "plum"]
     tim.pencolor(ae[random.randint(0,8)])
     tim.setheading(90)
     tim.forward(100)

def down():
     ae = ["cyan", "firebrick", "violet", "gold", "silver", "aquamarine", "lime", "green", "plum"]
     tim.pencolor(ae[random.randint(0,8)])
     tim.setheading(270)
     tim.forward(100)

def left():
     ae = ["cyan", "firebrick", "violet", "gold", "silver", "aquamarine", "lime", "green", "plum"]
     tim.pencolor(ae[random.randint(0,8)])
     tim.setheading(180)
     tim.forward(100)

def right():
     ae = ["cyan", "firebrick", "violet", "gold", "silver", "aquamarine", "lime", "green", "plum"]
     tim.pencolor(ae[random.randint(0,8)])
     tim.setheading(0)
     tim.forward(100)
def see(x, y):
     tim.penup()
def eee(x, y):
     tim.pendown()

tim = turtle.Turtle("turtle")
tim.speed(9)
tim.color("white")
tim.pensize(7)
turtle.listen()

turtle.onscreenclick(see, 1)  # 1:Left Mouse Button, 2: Middle Mouse Button
turtle.onscreenclick(eee, 3)

turtle.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")


turtle.mainloop()  # This will make sure the program continues to run 
