import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()

num_sides = 30
angle=360/num_sides
side_length=7

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()