# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:38:29 2017

@author: rohan
"""

import pandas as pd
import matplotlib.pyplot as plt
import os 
plt.style.use('ggplot')
#create a datafram

my_dict =  my_dict = {"Numbers":[1,2,3,4,5], "Fruit":["Apple","Orange","peer","Orange","Peach"]}
my_df = pd.DataFrame(my_dict)


#create an excel file 
my_df.to_excel('test1.xlsx', sheet_name = 'test1',index = False)
my_df.to_excel('test2.xlsx', sheet_name = 'test2',index = False)
my_df.to_excel('test3.xlsx', sheet_name = 'test3',index = False)

files = os.listdir(".")
xcel_files = []

for file in files:
    if file.endswith('.xlsx'):
        xcel_files.append(file)
print(xcel_files)


reread_data = []
for file in xcel_files:
    reread_data.append(pd.read_excel(file))

big_df = pd.concat(reread_data)

big_df.Fruit.value_counts().plot('bar',title = 'My bar chart with 3 times the Data')
