'''
Created on February 25, 2021
@author: David Pennington
'''
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

if __name__ == '__main__':
    test_url = "http://www.just-eat.co.uk/"
    post_code = "AR51 1AA"
    dish = "chicken"
    search_criteria = '[title = "New"]'
    wait_time = 15
    browser = "C:\\Selenium\\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(browser) # Open Chrome
    driver.maximize_window() # maximize the browser window
              
    driver.get(test_url) # Navigate to the test website
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".logo-image"))) # wait for the page to load before continuing with the test
    print ("page title is:", driver.title)
    
    # Search for restaurants in the postcode specified
    driver.find_element_by_name('postcode').send_keys(post_code) # enter the postal code
    driver.find_element_by_css_selector('[data-test-id = "find-restaurants-button"]').click() # click the Search button 
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id = "openrestaurants-count-heading"]'))) # wait for the number of restaurants to be displayed
    num_rest = driver.find_element_by_css_selector('[data-test-id = "openrestaurants-count-heading"]').text
    num_rest = int(re.sub("[^0-9]", "", num_rest)) #remove text, keep the numeric part, and convert to integer
    print (num_rest, 'restaurants found')
    
    # Search for restaurants in the specified postal code that serve the dish specified
    driver.find_element_by_id('dish-search').send_keys(dish) # enter the dish to search for
    driver.find_element_by_css_selector('[data-test-id = "unified-submit-button"]').click() # click the Search button 
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id = "openrestaurants-count-heading"]'))) # wait for the number of matching restaurants to be displayed
    num_dish = driver.find_element_by_css_selector('[data-test-id = "openrestaurants-count-heading"]').text
    num_dish = int(re.sub("[^0-9]", "", num_dish)) #remove text, keep the numeric part, and convert to integer
    print (num_dish, 'restaurant(s) found that serve', dish)
    
    # Select special offers from the filter
    search_filter = driver.find_element_by_css_selector(search_criteria)
    search_filter_text = search_filter.text
    search_filter_text = re.sub("\n.*$", "", search_filter_text)
    ActionChains(driver).move_to_element(search_filter).click(search_filter).perform()
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id = "openrestaurants-count-heading"]'))) # wait for the number of matching restaurants to be updated based on the filter change
    num_dish = driver.find_element_by_css_selector('[data-test-id = "openrestaurants-count-heading"]').text
    num_dish = int(re.sub("[^0-9]", "", num_dish)) #remove text, keep the numeric part, and convert to integer
    print (num_dish, 'restaurant(s) found that serve', dish, 'that are', search_filter_text )
    
    driver.quit() # Close the browser and end the session