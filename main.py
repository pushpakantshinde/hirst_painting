import turtle
import random

turtle.colormode(255)

my_turtle = turtle.Turtle()

color_list = [(236, 35, 108), (145, 28, 64), (239, 75, 35), (6, 148, 93), (231, 168, 40), (184, 158, 46),
              (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97),
              (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23),
              (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182),
              (180, 187, 211)]

#--------------------------------------------------------------------------------------------------------------------
# def color_filling():
#     fill_this_color = random.choice(color_list)
#     my_turtle.begin_fill()
#     my_turtle.fillcolor(fill_this_color)
#     my_turtle.circle(10)
#     my_turtle.end_fill()
#
# my_turtle.penup()
# my_turtle.goto(-400, -400)
# my_turtle.speed("fastest")
# vertical_shift = -400
#
# for y_range in range(10):
#     for x_range in range(10):
#
#         color_filling()
#
#         my_turtle.penup()
#         my_turtle.forward(50)
#         my_turtle.pendown()
#
#     my_turtle.penup()
#     vertical_shift += 50
#     my_turtle.goto(-400, vertical_shift)
#---------------------------------------------------------------------------------------------------------------------

# OR

my_turtle.penup()
my_turtle.goto(-400, -400)
my_turtle.speed("fastest")
vertical_shift = -400

for y_range in range(10):
    for x_range in range(10):
        fill_this_color = random.choice(color_list)
        my_turtle.dot(20, fill_this_color)
        my_turtle.forward(50)

    vertical_shift += 50
    my_turtle.goto(-400, vertical_shift)


screen = turtle.Screen()
screen.exitonclick()
