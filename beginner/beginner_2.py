# -*- coding: utf-8 -*-
"""
Beginner Script 2 - Functions, Parameters, and Numbers

Functions allow you to group blocks of code and assign it a name.  Functions
can be called over and over again to perform specific tasks.
"""

def add(x, y):
    return (x + y)

def subtract(x, y):
    return (x - y)
"""
1.) Functions are blocks of code with three important features. Most
importantly, they are assigned a name.  This name can be called later in the progam.
Secondly, they can be passed variables.  These variables can be used within
the scope (beginning to end) of the function to perform various operations.
Third, they can return a value to the calling program.

Create a multiply and divide function.
"""



"""
2.) When running the Python script, functions can be used to group blocks of
code and return values for us.

Call the subtract, multiply, and division.
"""
x_int = 2
y_int = 10
a = add(x_int, y_int)
print( 'Added: ' + str(a) )
# Another, and preferred way to format the string is to call the format function:
# print( 'Added: '.format(str(a)) )

"""
3.) There are two types of numbers in Python - integers and floating points.
In our previous lesson, we worked with integers.  Integers do not have a decimal,
while floating point numbers do.  This differentiation may not seem like much,
but to a computer it means a completely different way of storing the number in
memory.

Perform the above exercise, but assign x_fp and y_fp a number that includes a decimal.
"""
# x_fp = ...
# y_fp = ...

# Reassiging a to a different value.
# a = add(x_fp, y_fp)
# print( 'Added: '+ str(a) )
