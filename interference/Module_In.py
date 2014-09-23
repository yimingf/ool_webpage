'''
Created on Sep 23, 2014

@author: menghuan007
'''
from numpy import Inf
from operator import pos

class Light_source:
    maxx = -Inf
    maxy = -Inf
    minx = Inf
    miny = Inf
    w_length = 0
    def __init__(self,x = 0,y = 0,w_length = 0):
        self.x = x
        if (Light_source.maxx < x):
            Light_source.maxx = x
        if (Light_source.minx > x):
            Light_source.minx = x
        self.y = y
        if (Light_source.maxy < y):
            Light_source.maxy = y
        if (Light_source.miny > y):
            Light_source.miny = y
        Light_source.w_length = w_length
        

class Light_screen:
    def __init__(self,a = 0,b = 0,c = 0):
        self.a = a
        self.b = b 
        self.c = c 
        
class Lens:
    def __init__(self,pos = 0,focus=0):
        self.pos = pos
        self.focus = focus