# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

with open('drawing.txt', 'r') as file:
    for line in file:
        if "UP" in line:
            t.up()
        elif "DOWN" in line:
            t.down()
        else:
            x = float(line.split(" ")[0])
            y = float(line.split(" ")[1])
            t.goto(x, y)
            

# wait
turtle.Screen().exitonclick()

