# Author : Josephine Cuyo
# Course and Year : 2nd year BS-IT
# Filename : cuyo-probb.py
# Description : Write a program that reads an integer and prints the sequence of Fibonacci numbers
#               as a comma-separated list on a single line.
# Honor Code : I have not given nor received any unathorized help in
# completing this exercise. I am also well aware of the
# policies stipulated in the AdNU student handbook.


T = int(input());        # input number of test cases
a = 0               # first term for Fibonacci
b = 1               # second term for Fibonacci
c = 0
i = 1               # test case number
string_output = ""  # declaration of string

while (T != 0):      # loop for entering number of testcases
    n = int(input());                                   # user inputs n
    string_output += ("CASE ") + str(i) + (": ")        # case number is stored in string
    while (c < n+1):       # loop for fibonacci
        if (c < n):        # condition for placement of comma
            string_output += str(a) + ","               # nth fibonacci number is stored in the string
            fibo = a + b
            a = b          # fibonacci formula
            b = fibo
            c = c + 1
        else:
            string_output += str(a) + " "
            fibo = a + b
            a = b          # fibonacci formula
            b = fibo
            c = c + 1
    string_output += "\n"  # endline is stored in the string for new case
    n = 0
    a = 0
    b = 1                  # all numeric variables are reset for the new test case
    c = 0
    fibo = 0
    i = i + 1              # new test case number
    T = T - 1              # decrement for the loop to have an end

print(str(string_output))  # all cases are now printed
  
