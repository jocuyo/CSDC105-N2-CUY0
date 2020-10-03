# Author          : Josephine Cuyo
# Course and Year : 2nd Year BS-IT
# Filename        : geometry.py
# Description     : {A brief description of what this program does}
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

import math

def perimeter(a,b,c):       
    return a + b + c                                    # function where it returns the sum of all sides (the perimeter)

def triangle_heronsarea(a,b,c):
    s = (a+b+c)/2                                       # formula for the semi-perimeter wwhich is needed in computing the area
    heronsarea = math.sqrt(s*(s-a)*(s-b)*(s-c))         # formula in finding the area of the triangle
    return heronsarea                                   # function returns the computed value of herons area
