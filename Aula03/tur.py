# sunrise.py
import turtle
from collections import namedtuple
number_of_steps = 500
width = 1200
height = 800
# Create Named Tuple Classes
RangeLimits = namedtuple("RangeLimits", "start, end")
Colour = namedtuple("Colour", "red, green, blue")
sky_colour = RangeLimits(
    Colour(0 / 255, 0 / 255, 0 / 255),
    Colour(0 / 255, 191 / 255, 255 / 255),
)
petal_colour = RangeLimits(
    Colour(50 / 255, 50 / 255, 50 / 255),
    Colour(138 / 255, 43 / 255, 226 / 255),
)
flower_centre_colour = RangeLimits(
    Colour(30 / 255, 30 / 255, 30 / 255),
    Colour(255 / 255, 165 / 255, 0 / 255),
)
stem_colour = RangeLimits(
    Colour(15 / 255, 15 / 255, 15 / 255),
    Colour(34 / 255, 139 / 255, 34 / 255),
)
def calculate_colour_change(
    start: Colour,
    end: Colour,
    n_steps: int,
):
    red_step = (end.red - start.red) / n_steps
    green_step = (end.green - start.green) / n_steps
    blue_step = (end.blue - start.blue) / n_steps
    return Colour(red_step, green_step, blue_step)
# Set up the window for the animation
# Sky
sky = turtle.Screen()
sky.setup(width, height)
sky.tracer(0)
sky.title("Good morning…")
sky.bgcolor(sky_colour.start)
# Flower and Stem
flower = turtle.Turtle()
flower.hideturtle()
stem = turtle.Turtle()
stem.hideturtle()
stem.right(90)
stem.pensize(10)
def draw_flower(petal_col, flower_centre_col, stem_col):
    stem.clear()
    stem.color(stem_col)
    stem.forward(height / 2)
    stem.forward(-height / 2)
    flower.clear()
    flower.color(petal_col)
    # Draw petals
    for _ in range(6):
        flower.forward(100)
        flower.dot(75)
        flower.forward(-100)
        flower.left(360 / 6)
    # Draw centre of flower
    flower.color(flower_centre_col)
    flower.dot(175)
# Draw the initial flower using the starting colours
draw_flower(
    petal_colour.start,
    flower_centre_colour.start,
    stem_colour.start,
)
####
# Calculate step sizes needed for colour changes
sky_colour_steps = calculate_colour_change(
    sky_colour.start, sky_colour.end, number_of_steps
)
petal_colour_steps = calculate_colour_change(
    petal_colour.start, petal_colour.end, number_of_steps
)
flower_centre_colour_steps = calculate_colour_change(
    flower_centre_colour.start,
    flower_centre_colour.end,
    number_of_steps,
)
stem_colour_steps = calculate_colour_change(
    stem_colour.start, stem_colour.end, number_of_steps
)
####
# Start animation
current_sky_colour = sky_colour.start
current_petal_colour = petal_colour.start
current_flower_centre_colour = flower_centre_colour.start
current_stem_colour = stem_colour.start
for _ in range(number_of_steps):
    # Sky
    current_sky_colour = Colour(
        current_sky_colour.red + sky_colour_steps.red,
        current_sky_colour.green + sky_colour_steps.green,
        current_sky_colour.blue + sky_colour_steps.blue,
    )
    # Change the background to use the new colour
    sky.bgcolor(current_sky_colour)
    # Flower and Stem
    current_petal_colour = Colour(
        current_petal_colour.red + petal_colour_steps.red,
        current_petal_colour.green + petal_colour_steps.green,
        current_petal_colour.blue + petal_colour_steps.blue,
    )
    current_flower_centre_colour = Colour(
        current_flower_centre_colour.red
        + flower_centre_colour_steps.red,
        current_flower_centre_colour.green
        + flower_centre_colour_steps.green,
        current_flower_centre_colour.blue
        + flower_centre_colour_steps.blue,
    )
    current_stem_colour = Colour(
        current_stem_colour.red + stem_colour_steps.red,
        current_stem_colour.green + stem_colour_steps.green,
        current_stem_colour.blue + stem_colour_steps.blue,
    )
    # Draw the flower again with the new colours
    draw_flower(
        current_petal_colour,
        current_flower_centre_colour,
        current_stem_colour,
    )
    sky.update()
turtle.done()