''' Created on May 5, 2020
@author: Home
Test program to try out classes '''

from circle import Circle1
    
if __name__ == '__main__':
    c1 = Circle1('red', 1)
    print ('Color: ' ,c1.color)
    print ('Radius: ', c1.radius)
    print ('Area: ', c1.get_area())
    print (c1.x)
    print (c1.silly_stuff())
    print (c1.abc, '  ', c1.xyz)
    print (c1.__dict__)
    
    c2 = Circle1('blue', 2)
    print ('Color: ' ,c2.color)
    print ('Radius: ', c2.radius)
    print ('Area: ', c2.get_area())
    print (c2.x)
    print (c2.silly_stuff())
    print (c2.abc, '  ', c2.xyz)
    print (c2.__dict__)
    
    c3 = Circle1('green', 3.5)
    print ('Color: ' ,c3.color)
    print ('Radius: ', c3.radius)
    print ('Area: ', c3.get_area())
    print (c3.x)
    print (c3.silly_stuff())
    print (c3.abc, '  ', c3.xyz)
    print (c3.__dict__)