'''
Created on May 29, 2020

@author: Home
'''
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    URL = 'https://eastcourtfordlincoln.com/used-inventory/make/ford/price/13999-50498/mileage/411-96089/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    prices = soup.find_all('strong')
    cars = soup.find_all('h3')
    count = 0
    car_data = []

    for car in cars:
        car_data.append((car.text.strip()+ prices[count].text.strip())) # remove spaces and match up car desc with prices
        count +=1
    
    car_data = sorted(car_data)
    for car in car_data:
         print (car)
            
    print ("total cars: " , count)