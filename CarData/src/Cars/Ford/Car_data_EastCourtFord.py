'''
Created on July 10, 2020
@author: DNP Enterprises Inc.
Since the next page icon is not easily readable, the total number of cars and cars displayed per page is used to navigate this site
'''
from datetime import datetime
import re
#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Quotes.Excel_utils2 import Excel_utils2
from Cars.CreateDealerSheet2 import CreateDealerSheet
from Cars.browser_start import browser_start

if __name__ == '__main__':
    file_in = 'C:/Users/Home/Desktop/Cars/CarData.xlsx'
    data_in = Excel_utils2(file_in, 'Ford', 'in')
    file_out = data_in.sht.cell(2,7).value
    dealer = data_in.sht.cell(2,1).value
    base_url = data_in.sht.cell(2,2).value
    dealer_id = (data_in.sht.cell(2,3).value).split() # convert to a list for use later
    date_time = datetime.now().strftime('%Y %B %d %I %M %p') # get the date and time
    data_out = Excel_utils2(' ', date_time, 'out') # set the spreadsheet tab to the dealer name
    driver = browser_start(base_url, True) # run browser in headless mode
    #driver = browser_start(base_url, False) # run browser in headless mode
    #driver = browser_start(base_url) # run browser in non-headless, incognito mode
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.total-results-preview'))) # wait for number of cars to be displayed
    print (driver.title)
    num_cars = driver.find_element_by_css_selector('div.total-results-preview').text
    #test1 = driver.find_element_by_css_selector('span.text-lg').text  #can also find number of car with this
    num_cars = int(re.sub("[^0-9]", "", num_cars))
    print ("Number of cars found on site: " , num_cars)
    cars_per_page = 50
    num_pages = num_cars // cars_per_page
    if num_cars % cars_per_page >0: # if the number of cars per page doesn't divide evenly into the total number of cars, we need one more page
        num_pages += 1
    count = 0
    zero = 0
    car_info = []
    print ("# of pages: ", num_pages)

    for page in range(num_pages):
        if page >0:
            url = base_url[:-1] + str(page+1) # remove the last character of the base url and add the next page number
            print (url)
            driver.get(url) # Navigate to the test website
            # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".lg\:leading-tight"))) # wait for number of cars to be displayed
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.total-results-preview'))) # wait for number of cars to be displayed
            #sleep(4)

        # car_desc_raw = driver.find_elements_by_css_selector('h3' '.text-black')
        car_desc_raw = driver.find_elements_by_css_selector('h6' '.vehicle-title')
        prices = driver.find_elements_by_tag_name('strong')
        stock = driver.find_elements_by_css_selector('div.w-full.text-center.font-light.text-sm.py-1.mt-2.md\:flex.md\:flex-wrap.md\:justify-center > div > p')
        details_links = driver.find_elements_by_css_selector('.mx-auto.flex [href]')
                    
        for index, car in enumerate(car_desc_raw):
            car_name = (car.text +" ").split()[:4] # keep the year, make, and model, remove the rest
            year = car_name[0].split() # convert the year to a list
            make = car_name[1].split() # convert make to a list
            model = car_name[2:] # model is already a list
            model = [' '.join(model)] # merge the model into one list element
            car_desc = year + make + model
            price = re.sub("[$,]", "", prices[index].text) # remove $ and ',' from the price
            if (not price.isdigit()): # if the price is "Please call" or something non-numeric, set the price to 0
                price = '0'
                zero += 1
            price = price.split() # convert to a list
            stock_num = (stock[index].text[8:]).split() # remove "Stock #:" and keep the stock #
            link = (details_links[index].get_attribute('href')).split()
            print (index,":", car_desc, price, stock_num, link)
            car_info.append(dealer_id + car_desc + price + stock_num + link)
            count +=1
 
    print ("Total cars processed: ", count, " Total unpriced cars: ", zero)
            
    car_info = sorted(car_info)
    for index, i in enumerate(car_info):
        print (index, ":", i)
        
    print ("Saving data in a spreadsheet....", file_out)
    CreateDealerSheet(data_out, car_info, date_time)
    print (dealer, "Total cars: " , count)
    data_out.save_file(file_out)
       
    driver.quit() # Close the browser and end the session
