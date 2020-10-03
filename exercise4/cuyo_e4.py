# Author          : Josephine Cuyo
# Course and Year : 2nd Year BS-IT
# Filename        : cuyo_e4.py
# Description     : {A brief description of what this program does}
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

def CheckingSides(a,b,c):                               
    if ((a + b) <= c) or ((b + c) <= a) or ((a + c) <= b): 
        return False                                     # function that returns True if the sides are valid, otherwise False
    else:                                   
        return True


a, b, c = input("Enter the sides of the triangle: ")    # user inputs the values of the side of the triangles
a = float(a)
b = float(b)                                            # a, b, and c are of type float
c = float(c)

if CheckingSides(a,b,c):
    P = perimeter(a,b,c)                                # the perimeter and area are stored in the variables P and A
    A = triangle_heronsarea(a,b,c)                      # for the function
    print("Perimeter: " + format(P,'.2f'))              # prints the perimeter in 2 decimal places
    print("Area: " + format(A,'.2f'))                   # prints the area in 2 decimal places
else:
    print("Error: Invalid input")                       # if the lengths are invalid, program prints "Error: Invalid input"
