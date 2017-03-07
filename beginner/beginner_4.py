# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:52:42 2017

@author: rohan
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
plt.style.use('ggplot')

my_dict = {"Numbers":[1,2,3,4,5], "Fruit":["Apple","Orange","peer","Orange","Peach"]}
my_df = pd.DataFrame(my_dict)

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
