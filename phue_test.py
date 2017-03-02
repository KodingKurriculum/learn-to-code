# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:07:29 2017

@author: rohan
"""

from phue import Bridge
import time 
b = Bridge('192.168.2.74')#
b.set_light([1,2,3],'bri',254)
b.set_light([1,2,3],'sat',180)

minutes = 10
cycle_secs = 10
maxhue = 65000
color_inc = maxhue/cycle_secs/10
tenths = minutes * 600

for inc in range(tenths):
    color = (inc*color_inc)%maxhue
    b.set_light(1,'hue',int(color),transitiontime = 1)
    b.set_light(1,'hue',int((color+maxhue/3)%maxhue),transitiontime = 1)
    b.set_light(1,'hue',int((color+2*maxhue/3)%maxhue),transitiontime = 1)
    time.sleep(0.1)
    if inc%10 == 0:
        print("\rTime remaining: {:3.0f} seconds".format(minutes*60-inc/10),end =" ")