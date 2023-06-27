# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard

print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))

# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

# The radius of the board
RADIUS = 160

# The radius of the inner circle
INNER_RADIUS = 6.35

# The radius of the outer circle
OUTER_RADIUS = 324.84

# The radius of the middle circle
MIDDLE_RADIUS = 107.95

# The radius of the triple ring
TRIPLE_RADIUS = 254

# The radius of the double ring
DOUBLE_RADIUS = 214

# The radius of the single ring
SINGLE_RADIUS = 174

# The radius of the bullseye
BULLSEYE_RADIUS = 6.35

# The radius of the outer bullseye
OUTER_BULLSEYE_RADIUS = 31.75

# The radius of the inner bullseye
INNER_BULLSEYE_RADIUS = 15.9

# The radius of the outer triple ring
OUTER_TRIPLE_RADIUS = 294



#print(score)

# The score is 0 if the dart is outside the board
score = 0

# The score is 25 if the dart is in the bullseye
if x**2 + y**2 <= BULLSEYE_RADIUS**2:
    score = 25

# The score is 50 if the dart is in the outer circle
elif x**2 + y**2 <= OUTER_RADIUS**2:
    score = 50

# The score is 25 if the dart is in the middle circle
elif x**2 + y**2 <= MIDDLE_RADIUS**2:
    score = 25

# The score is 0 if the dart is in the inner circle
elif x**2 + y**2 <= INNER_RADIUS**2:
    score = 0

# The score is 0 if the dart is in the triple ring
elif x**2 + y**2 <= TRIPLE_RADIUS**2:
    score = 0

# The score is 0 if the dart is in the double ring
elif x**2 + y**2 <= DOUBLE_RADIUS**2:
    score = 0

# The score is 0 if the dart is in the single ring
elif x**2 + y**2 <= SINGLE_RADIUS**2:
    score = 0

# The score is 0 if the dart is in the bullseye
elif x**2 + y**2 <= BULLSEYE_RADIUS**2:
    score = 0

# The score is 0 if the dart is outside the board
else:
    score = 0

print(score)