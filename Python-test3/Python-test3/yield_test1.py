'''
Created on May 27, 2020
test how yield works
@author: Home
'''
def table(n):
    for i in range(1,11):
        yield n*i
        i = i+1

for i in table(15):
    print (i)