# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:52:42 2017

@author: rohan
"""
"""To import a package in python use the key word "import"

    example import <package>
    or import <package> as <object>

    or form <import> <object>
"""

import pandas as pd # here we are importing pandas
import matplotlib.pyplot as plt
import os #This module provides a portable way of using operating system dependent functionality.
plt.style.use('ggplot')
""" form the previous section we learned how to create dictionaries with Keys that has values
    create a new dict call it Mydict2 and have  Fruits as the key also add a list with numbers from 0 to 10
 eg. "Fruit":[1,2,3....]
     then try to plot the data.

"""
my_dict = {"Numbers":[1,2,3,4,5]}
my_df = pd.DataFrame(my_dict) #The dataFrame is like a excel sheet
#create a Data frame
plt.figure()
my_df.Numbers.plot(title = 'My Numbers line chart')
my_df = pd.DataFrame(my_dict)
#create an excel file
my_df.to_excel('test1.xlsx',sheet_name = 'test1',index = False)
#read an excel file
reread_my_df = pd.read_excel('test1.xlsx')
plt.figure()
reread_my_df.Numbers.plot(title = 'My reread data')
""" Try to create your own plot"""
my_dict2 = {"Fruit":[0,1,3,4,5,6,7,8,9,10]}
my_df2 = pd.DataFrame(my_dict2)
plt.figure()
my_df2.Fruit.plot(title = 'My Fuits line chart')
my_df2 = pd.DataFrame(my_dict2)
