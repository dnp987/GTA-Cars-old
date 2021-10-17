'''
Created on May 28, 2020

@author: Home
'''
from bs4 import BeautifulSoup

with open("C:/temp/test.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print (soup)

for link in soup.find_all('a'):
    print (link.get('href'))
print ("test2:")
print (soup.find_all("a", class_= "sister"))