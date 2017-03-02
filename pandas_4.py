# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:25:08 2017

@author: rswaby
"""
import quandl
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
mydata = quandl.get("WIKI/AAPL")
mydata["Adj. Close"].plot()
"""In the terminal look at In[n] mydata hit enter."""