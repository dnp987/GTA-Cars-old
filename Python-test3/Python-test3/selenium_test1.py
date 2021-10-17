'''
Created on Jun 1, 2020

@author: Home

Proof of concept for finding multiple tags and text
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://eastcourtfordlincoln.com/used-inventory/make/ford/price/13999-50498/mileage/411-96089/'

browser = "C:\\Selenium\\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(browser) 
driver.get(URL) # Navigate to the test website
wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(5) > div.mx-auto > div > main > div.container.mx-auto.text-center.pb-4.page-main-title > h1'))) # wait for "USED VEHICILES" to appear
cars = driver.find_elements_by_tag_name("h3")
count = 0
prices = driver.find_elements_by_tag_name("strong")
for price in prices:
    print (count, " ", cars[count].text, " ", price.text)
    count += 1
    
driver.close()