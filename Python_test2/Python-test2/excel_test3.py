'''
Created on May 8, 2020

@author: Home
'''
import openpyxl

if __name__ == '__main__':
    car_data_file = 'C:/Users/Home/Desktop/Cars/Ford/CarPrices-YorkdaleFord.xlsx'
    dealer_wkbk = openpyxl.load_workbook(car_data_file)
    dealer_sht = dealer_wkbk.active
    print (dealer_sht)
    for row in dealer_sht.rows:
        print (row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value)