
# Joy of Coding Minicourse Day 3 Part 2

# by Anthony Rodriguez


# Quintessential first program

#print("Hello World!")

# Begin Day 2

import turtle # brings in turtle module / library

turtle.color("blue") # changes turtle pen color to blue

'''turtle.forward(50) # moves turtle in a specific direction relative to where it is facing
turtle.right(120) # rotates turtle a certain number of degrees
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(120)'''


'''tri_side = 80

turtle.forward(tri_side) # moves turtle in a specific direction relative to where it is facing
turtle.right(120) # rotates turtle a certain number of degrees
turtle.forward(tri_side)
turtle.right(120)
turtle.forward(tri_side)
turtle.right(120)

turtle.forward(tri_side)
turtle.left(120)
turtle.forward(tri_side)
turtle.left(120)
turtle.forward(tri_side)
turtle.left(120)'''


tri_side1 = 100

for side in range(3):
    turtle.forward(tri_side1)
    turtle.left(120)



turtle.Screen().exitonclick() # prevents turtle graphics from closing until you click on it