# -*- coding: utf-8 -*-
"""
Beginner Script 4 - Imports, Pandas, and Matplotlib

In this script, we'll learn to import third party libraries, read an excel sheet,
plot values to a graph, and write to an excel sheet.

1.) We include other libraries that people have built by using the special
keyword "import".  At the beginning of the setup, you were asked to run the
command 'conda install pandas matplotlib ...'.  This command installed the
libraries on your computer so that they can be imported.
"""
import pandas as pd # here we are importing pandas and renaming it to 'pd'
import numpy as np

def plotDataFrame():
    """
    2.) A dictionary is a special python object that allows you to map a key to a
    list of values.  You can then later look up the list of values through this key.
    """
    my_dict = {
            "Numbers": [4, 1, 5, 2, 3],
            "Names": np.random.rand(5)
        }
    
    """
    3.) A dictionary is a special python object that allows you to map a key to a
    list of values.  You can then later look up the list of values through this key.
    
    The DataFrame is like a excel sheet
    """
    my_df = pd.DataFrame(my_dict)
    
    """
    4.) Data Frames are great because they have useful functions you can use to
    interact with your dataset like 'sort' and 'plot'
    
    DataFrame.sort(['column_1', 'column_2'], ascending=[1,0])
    DataFrame.plot(style=['o','rx'], title = '...')
    """
    # sort ...
    
    # then plot



    
def plotExcel():  
    """
    4.) DataFrames also have built in Excel functionality, like creating a file
    and reading from one.
    
    DataFrame.to_excel('file_name.xlsx', sheet_name='sheet_name', index=False)
    DataFrame.read_excel('file_name.xlsx')
    """
    # create a dictionary of numbers
    
    # write to the file
    
    # read from the file
    
    # sort descending
    
    # plot the results
    
    """
    Your assignment is to write a function that 
        - accepts an Excel file name as a parameter, 
        - reads the Excel file, 
        - and plot a specific column.
    """
