# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Sample code form conor
"""

from numpy.random import rand
import matplotlib.pyplot as plt
plt.style.use('ggplot')

for color in ['red','green', 'blue']:
    n = 750
    x,y = rand(2,n)#
    scale = 200.0*rand(n)
    plt.scatter(x,y,c=color,s = scale, 
                label = color, alpha = 0.3, edgecolor = 'none')
plt.legend()
plt.grid(True)
plt.show()

"""
In the Terminal 
>>> 2+2
>>>4
>>>var = 3412
>>>100*var
>>> 100 * somVar#undefined variable 
>>>"""