#Gulzat Kaipova
#8/4/2023

#This program takes user inputs for the number of sides, side length, line color, 
#and fill color of a regular polygon, and then draws and fills the polygon accordingly.

import turtle

# Ask user for input
num_sides = int(input("Enter the number of sides for the polygon: "))
side_length = int(input("Enter the length of each side: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

# Initialize the turtle
window = turtle.Screen()
window.bgcolor("white")
polygon_turtle = turtle.Turtle()

# Set line and fill colors
polygon_turtle.color(line_color)
polygon_turtle.fillcolor(fill_color)

# Draw the polygon
polygon_turtle.begin_fill()
for _ in range(num_sides):
    polygon_turtle.forward(side_length)
    polygon_turtle.left(360 / num_sides)
polygon_turtle.end_fill()

# Close the window on click
window.exitonclick()
