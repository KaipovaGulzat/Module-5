#Gulzat Kaipova
#8/4/2023

#The program uses the turtle graphics library to create a creative and customizable picture by experimenting with various turtle methods, 
#allowing for the creation of unique visual patterns and designs.

import turtle
import random

# Set up the turtle
window = turtle.Screen()
window.bgcolor("white")
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Fastest drawing speed

# Define colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw a colorful spiral pattern
for _ in range(200):
    spiral_turtle.color(random.choice(colors))
    spiral_turtle.forward(100)
    spiral_turtle.left(123)

# Hide the turtle and exit on click
spiral_turtle.hideturtle()
window.exitonclick()
