import turtle as t
#from turtle import Turtle, Screen
import random
tim = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("(red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

#for _ in range(4):
 #   tim.forward(100)
  #  tim.left(90)

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)
for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


