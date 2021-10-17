'''
Created on May 6, 2020

@author: Home
'''
from cmath import pi
class Circle1:
    abc = 123
    xyz = 456
    
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius
        self.x = (radius *2)/3

    def get_area(self):
        return (self.radius *2) * pi
    
    def silly_stuff(self):
        y = self.abc+self.xyz/2
        print ('This is silly: ')
        return (y)