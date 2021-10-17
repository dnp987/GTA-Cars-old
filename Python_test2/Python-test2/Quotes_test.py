'''
Created on 03Apr2020

@author: Home
'''
from Excel_utils2 import Excel_utils2
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__=='__main__':
    file_in = 'C:/temp/test-parameters.xlsx'
    file_out = 'C:/temp/Quotes-test.xlsx'
    data_in = Excel_utils2(file_in, 'test_parameters', 'in')
    
    # Get account # and password
    target_url = data_in.sht.cell(row = 2, column = 2).value
    acc_num = data_in.sht.cell(row = 3,column = 2).value
    passwd = data_in.sht.cell(row = 4,column = 2).value
    
    data_in = Excel_utils2(file_in, 'CA_Symbols', 'in') # Set the work sheet to the test stock symbols
        
    browser = "C:\\Selenium\\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    # Open Chrome and navigate to the test website
    driver = webdriver.Chrome(browser)
    driver.get(target_url)
    page_title = "BMO InvestorLine" 
    assert page_title in driver.title
    print ("Loading the target page...")
    # Enter account #
    log_in = driver.find_element_by_id("loginText")
    log_in.send_keys(acc_num)

    # Enter password
    password = driver.find_element_by_name("password")
    password.send_keys(passwd)

    # Click log in button to log in
    # driver.implicitly_wait(10) # seconds
    log_in_button = driver.find_element_by_id("sasi_btn").click()
    wait = WebDriverWait(driver, 10)
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # get the date and time
    
    data_out = Excel_utils2(' ', 'Quotes', 'out')
    data_out.set_cell(1, 1, "Symbol", "Arial", True, 12)
    data_out.set_cell(1, 2, "Last", "Arial", True, 12)
    data_out.set_cell(1, 3, "Bid", "Arial", True, 12)
    data_out.set_cell(1, 4, "Ask", "Arial", True, 12)
    data_out.set_cell(1, 5, "High", "Arial", True, 12)
    data_out.set_cell(1, 6, "Low", "Arial", True, 12)
    data_out.set_cell(1, 7, "Open", "Arial", True, 12)
    data_out.set_cell(1, 8, "Prev. Close", "Arial", True, 12)
    data_out.set_cell(1, 9, 'Date and time:', "Arial", True, 12)
    data_out.set_cell(1, 10, date_time, "Arial", False, 10)

    i=0
    for row in data_in.sht.rows:
        i+=1
        if (i == 1): # skip the 1st row, it contains headings
            continue
        
        # Wait for the Quotes & Tools menu item to appear
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav_quotes_main > a:nth-child(1)")))
        driver.find_element_by_css_selector("#nav_quotes_main > a:nth-child(1)").click() # click on Quotes & Tools
        # Wait for the Symbol text box to appear
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.paddingLeft25:nth-child(2) > input:nth-child(2)")))
        symbol = driver.find_element_by_css_selector("div.paddingLeft25:nth-child(2) > input:nth-child(2)")
        
        #test_symbol = data_in.sht.cell(row =i, column =1).value
        test_symbol = row.value
        symbol.send_keys(test_symbol, Keys.RETURN) # enter a symbol and get a quote
        
        # get a quote but wait for the "Summary" tab to appear
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page_navigation > div:nth-child(1) > a:nth-child(1)")))
        
        last_price = driver.find_element_by_css_selector(".brownContainer > div:nth-child(1) > span:nth-child(1)").get_attribute("innerText")
        bid_price = driver.find_element_by_css_selector("#table1 > table > tbody > tr.tableRowBG > td:nth-child(2)").get_attribute("innerText")
        ask_price = driver.find_element_by_css_selector("#table1 > table > tbody > tr:nth-child(2) > td:nth-child(2)").get_attribute("innerText")
        high = driver.find_element_by_css_selector("#table1 > table > tbody > tr.tableRowBG > td:nth-child(4)").get_attribute("innerText")
        low =  driver.find_element_by_css_selector("#table1 > table > tbody > tr:nth-child(2) > td:nth-child(4)").get_attribute("innerText")
        open_price = driver.find_element_by_css_selector("#table1 > table > tbody > tr.tableRowBG > td:nth-child(6)").get_attribute("innerText")
        prev_close = driver.find_element_by_css_selector("#table1 > table > tbody > tr:nth-child(2) > td:nth-child(6)").get_attribute("innerText")
        
        data_out.set_cell(i, 1, test_symbol, "Arial", False, 10)
        data_out.set_cell(i, 2, last_price, "Arial", False, 10)
        data_out.set_cell(i, 3, bid_price, "Arial", False, 10)
        data_out.set_cell(i, 4, ask_price, "Arial", False, 10)
        data_out.set_cell(i, 5, high, "Arial", False, 10)
        data_out.set_cell(i, 6, low, "Arial", False, 10)
        data_out.set_cell(i, 7, open_price, "Arial", False, 10)
        data_out.set_cell(i, 8, prev_close, "Arial", False, 10)
          
    data_out.save_file(file_out)
    print ("Test ending ...")
    driver.quit()