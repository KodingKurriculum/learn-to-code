# -*- coding: utf-8 -*-
"""
Beginner Script 3 - Lists, and Dictionaries

Functions allow you to group blocks of code and assign it a name.  Functions
can be called over and over again to perform specific tasks and return values
back to the calling program.
"""
"""
1.) Lists (also known as an Array) are great for storing a series of information.
You can iterate the list to access its contents, or specify a single value. Python
is zero-based, in that each position in the array is given a number from 0 to the
last element.
c
Add your name to the list, then have the script print your name.
"""
my_list = ['Karl', 'Karly', 'Kristoph', 'Kurt']
# print(...)

"""
2.) You may iterate the list using the "for loop" again.

Iterate the list of names and print out.
"""
# for name in ...:


"""
2.) Dictionaries are even more useful in that they can store key/value pairs of
information. As you may notice, the dictionary below looks a lot like an Excel
header with a list of values below.

Add my_list to the dictionary
"""
my_dict = {
    "Numbers": [1, 2, 3, 4, 5],
    "Fruit": ["Apple", "Orange", None, "Orange", "Peach"]
}


"""
3.) Dictionaries have key/value pairs which is useful for looking information up
based on a known key.  You can do this using the syntax my_dict['key'].

Look up the list of fruits from my_dict, and print the first fruit out.
"""
# fruits = ...


"""
4.) Python is an object-oriented language, and every variable has a group of
functions that you may call.  To iterate the list of dictionary key/value
pairs, we need to call the dictionary's .items() function, such as my_dict.items().

Iterate the list of key/value pairs and print them out.
"""
def printValues(dict):
    # for key, value in ...:
    #   print("My favorite {0} is {1}".format(key, value))
