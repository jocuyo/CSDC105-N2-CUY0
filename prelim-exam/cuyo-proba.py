# Author : Josephine Cuyo
# Course and Year : 2nd year BS-IT
# Filename : cuyo-proba.py
# Description : Write a program that prints a triangle
#               shape composed of specific ASCII character.
# Honor Code : I have not given nor received any unathorized help in
# completing this exercise. I am also well aware of the
# policies stipulated in the AdNU student handbook.

T = int(input())                    # user inputs number of test cases
spaces = 1                  
str_triangle = ""                   # a string named str_triangle is declared
casenum = 1                         # case number 


while (T!=0):
    k, c = input().split()          # user enters number of rows and ascii character to be printed and input.split() is needed ta whitespace lang ang nagseseparate
    k = int(k)                      # k is turned into an integer
    str_triangle += ("CASE " + str(casenum) + ":\n")
    for i in range(0,k):            # loop for row of characters
        for j in range(0,k-i-1):    # loop for the no of spaces kasi equilateral triangle and the number of spaces are decreasing
            str_triangle += (" ")   # the space is stored
        for j in range(0,2*i+1):    # loop for the ascii character
            str_triangle += (c)     # the ascii character is stored in the string
        str_triangle += ("\n")      
    T = T - 1                       # para may end ang loop so the testcase decrements
    casenum += 1                    # case number increases by one depending on the number of test cases
print(str_triangle)                 # all of the cases are printed

