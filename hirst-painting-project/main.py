import colorgram
from turtle import Turtle, Screen
import turtle as turtle_module
import random

turtle_module.colormode(255)

# Extract 6 colors from an image.
colors = colorgram.extract('photo47.jpg', 30)
rgb_colors=[]
TURTLE_SIZE = 20

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

tim = Turtle()
tim.shape("turtle")
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()
