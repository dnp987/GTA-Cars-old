'''
Created on 19May2020

@author: DNP Enterprises Inc.
'''
from Excel_utils2 import Excel_utils2
import unittest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Quotes(unittest.TestCase):
    def setUp(self):
        self.file_in = 'C:/temp/test-parameters.xlsx'
        self.file_out = 'C:/temp/Quotes-test2.xlsx'
        self.data_in = Excel_utils2(self.file_in, 'test_parameters', 'in')
        self.data_out = Excel_utils2(' ', 'Quotes', 'out')
        # Get account # and password
        self.target_url = self.data_in.sht.cell(row = 2, column = 2).value
        self.acc_num = self.data_in.sht.cell(row = 3,column = 2).value
        self.passwd = self.data_in.sht.cell(row = 4,column = 2).value
        browser = "C:\\Selenium\\chromedriver.exe"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(browser) # Open Chrome

    def test_get_quotes(self):
        self.data_in = Excel_utils2(self.file_in, 'CA_Symbols', 'in') # Set the work sheet to the test stock symbols
        # Navigate to the test website
        self.driver.get(self.target_url)
        page_title = "BMO InvestorLine - Account Access" 
        self.assertEqual(page_title, self.driver.title)
        print ("Loading the target page...")
        # Enter account #
        log_in = self.driver.find_element_by_id("loginText")
        log_in.send_keys(self.acc_num)

        # Enter password
        password = self.driver.find_element_by_name("password")
        password.send_keys(self.passwd)

        # Click log in button to log in
        # driver.implicitly_wait(10) # seconds
        log_in_button = self.driver.find_element_by_id("sasi_btn").click()
        wait = WebDriverWait(self.driver, 10)
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # get the date and time
            
        self.data_out.set_cell(1, 1, "Symbol", "Arial", True, 12)
        self.data_out.set_cell(1, 2, "Last", "Arial", True, 12)
        self.data_out.set_cell(1, 3, "Bid", "Arial", True, 12)
        self.data_out.set_cell(1, 4, "Ask", "Arial", True, 12)
        self.data_out.set_cell(1, 5, "High", "Arial", True, 12)
        self.data_out.set_cell(1, 6, "Low", "Arial", True, 12)
        self.data_out.set_cell(1, 7, "Open", "Arial", True, 12)
        self.data_out.set_cell(1, 8, "Prev. Close", "Arial", True, 12)
        self.data_out.set_cell(1, 9, 'Date and time:', "Arial", True, 12)
        self.data_out.set_cell(1, 10, date_time, "Arial", False, 10)

        i=0
        for row in self.data_in.sht.rows:
            i+=1
            if (i == 1): # skip the 1st row, it contains headings
                continue
        
            # Wait for the Quotes & Tools menu item to appear
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav_quotes_main > a:nth-child(1)")))
            self.driver.find_element_by_css_selector("#nav_quotes_main > a:nth-child(1)").click() # click on Quotes & Tools
            # Wait for the Symbol text box to appear
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.paddingLeft25:nth-child(2) > input:nth-child(2)")))
            symbol = self.driver.find_element_by_css_selector("div.paddingLeft25:nth-child(2) > input:nth-child(2)")
            test_symbol = self.data_in.sht.cell(row =i, column =1).value
            symbol.send_keys(test_symbol, Keys.RETURN) # enter a symbol and get a quote
        
            # get a quote but wait for the "Summary" tab to appear
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page_navigation > div:nth-child(1) > a:nth-child(1)")))
        
            last_price = self.driver.find_element_by_css_selector(".brownContainer > div:nth-child(1) > span:nth-child(1)").get_attribute("innerText")
            bid_price = self.driver.find_element_by_css_selector("#table1 > table > tbody > tr.tableRowBG > td:nth-child(2)").get_attribute("innerText")
            ask_price = self.driver.find_element_by_css_selector("#table1 > table > tbody > tr:nth-child(2) > td:nth-child(2)").get_attribute("innerText")
            high = self.driver.find_element_by_css_selector("#table1 > table > tbody > tr.tableRowBG > td:nth-child(4)").get_attribute("innerText")
            low =  self.driver.find_element_by_css_selector("#table1 > table > tbody > tr:nth-child(2) > td:nth-child(4)").get_attribute("innerText")
            open_price = self.driver.find_element_by_css_selector("#table1 > table > tbody > tr.tableRowBG > td:nth-child(6)").get_attribute("innerText")
            prev_close = self.driver.find_element_by_css_selector("#table1 > table > tbody > tr:nth-child(2) > td:nth-child(6)").get_attribute("innerText")
        
            self.data_out.set_cell(i, 1, test_symbol, "Arial", False, 10)
            self.data_out.set_cell(i, 2, last_price, "Arial", False, 10)
            self.data_out.set_cell(i, 3, bid_price, "Arial", False, 10)
            self.data_out.set_cell(i, 4, ask_price, "Arial", False, 10)
            self.data_out.set_cell(i, 5, high, "Arial", False, 10)
            self.data_out.set_cell(i, 6, low, "Arial", False, 10)
            self.data_out.set_cell(i, 7, open_price, "Arial", False, 10)
            self.data_out.set_cell(i, 8, prev_close, "Arial", False, 10)
            
    def  tearDown(self):
        self.data_out.save_file(self.file_out)
        self.driver.quit()
        print ("Test ending ...")    
    
if __name__== "___main__":
    unittest.main()