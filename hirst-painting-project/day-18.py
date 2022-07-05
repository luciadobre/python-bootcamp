from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")


######################################
#   Dotted line
# for i in range(4):
#     tim.forward(30)
#     tim.penup()
#     tim.forward(30)
#     tim.pendown()

######################################
# Shapes drawing
def change_color(turtle):
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)


change_color(tim)
######################################
# sides = 3
#
# while sides < 11:
#     for i in range(0, sides):
#         tim.forward(100)
#         tim.right(360 / sides)
#     change_color(tim)
#     sides += 1
######################################

orientation = [0, 90, 180, 270]
tim.speed(0)


######################################
# Random path colored
# tim.pensize(10)

# for i in range(0, 100):
#     tim.setheading(random.choice(orientation))
#     tim.forward(70)
#     change_color(tim)
######################################

# Draw Spirograph
# def circles(number_circles):
#     final_circle = 360 / number_circles
#     return final_circle
#
#
# for i in range(360):
#     tim.circle(100)
#     tim.right(circles(40))
#     change_color(tim)

screen = Screen()
screen.exitonclick()
