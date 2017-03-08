# -*- coding: utf-8 -*-
"""
Beginner Script 1 - Hello World!

This script is your first program.  You can run it in Spyder using the
play button on the menu above!
"""

1.) The triple double-quote allows you to use multi-line comments.  A pound (#)
sign is used for single line comments.  These lines will be ignored!

Comment this section out.


"""
2.) Variables are created and assigned values using the equals (=) sign.
Hello World is called a String. Strings are denoted by single or double quotes
and represent a series of characters.

Go ahead and uncomment the following line by deleting the pound (#) sign.
"""
# hello = 'Hello World!'

"""
3.) The print(string) function is a part of the standard Python library, and prints
to the console whatever contents are passed into it.  This function is useful
for debugging.

Print Hello World! by passing in the variable 'hello'
"""
print('')


"""
4.) The 'for loop' allows you to iterate over a series of values.  In this
example, we're looping through a set of numbers by using the range() Python
function.

Have this program run through numbers 10 to 20
"""
times = 10                      # iterate ten times!
for i in range(0, times):
    if (i == 1):                    # if statements use condition blocks to determine which code branch to execute
        print("First time!")
    elif (i == times):
        print("Last time!")         # Last time! doesn't print.  Why?
    else:
        print(hello+" "+str(i))     # use a plus sign to concatenate strings together into one

    """
    5.) Whoa! Why did we indent?! Indentations are used for blocks(sections) of
    of code. In this case, anthing that is indented after the 'for loop' statement
    is executed during each loop.
    """
