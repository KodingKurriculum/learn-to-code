# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:38:43 2017

@author: rswaby
"""

import pandas as pd
import matplotlib.pyplot as plt 
plt.style.use('ggplot')

#read html table 
tables = pd.read_html("http://www.bbc.com/sport/football/premier-league/table")
pl = tables[0]

pl.drop(["last 10  games results","Match Status","Unnamed: 0"],
        axis = 1, inplace = True)
pl.drop(20,inplace = True)
pl['Pts'] = pl['Pts'].astype(int)
pl.set_index('Team',inplace = True)



f,ax = plt.subplot()
f.subplots_adjust(left = 0.1, right = 0.9, bottom = 0.3)
pl['Pts'].plot('bar',ax = ax)
ax.set_ylabel("Points")
f.show()
"""
\raise ImportError("html5lib not found, please install it")

ImportError: html5lib not found, please install it"""
