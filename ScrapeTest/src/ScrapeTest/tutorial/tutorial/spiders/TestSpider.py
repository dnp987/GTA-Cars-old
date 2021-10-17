'''
Created on Jun 11, 2020

@author: Home
'''
import scrapy
import logging
from datetime import datetime
from scrapy.crawler import CrawlerProcess
from Quotes.Excel_utils2 import Excel_utils2

class TestSpider(scrapy.Spider):
    name = "TestSpider"
    file_in = 'C:/Users/Home/Desktop/Cars/CarData.xlsx'
    file_out = 'C:/Users/Home/Desktop/Cars/CarPrices-EastCourtFordLincoln.xlsx'
    data_in = Excel_utils2(file_in, 'Dealers', 'in')
    dealer = data_in.sht.cell(2,1).value
    URL = data_in.sht.cell(2,2).value
    date_time = datetime.now().strftime('%Y-%B-%d %I:%M %p') # get the date and time
    data_out = Excel_utils2(' ', dealer, 'out') # set the spreadsheet tab to the dealer name
    start_urls = URL.split() # scrapy requires the URL string to be a list
    
    def parse(self, response):
        msg = "***"+self.name+"***"
        logging.log(logging.INFO, msg)
                       
        #for info in (response.css('title::text').getall()):
        #    print ("*** title text:" + info)
        #print (response.xpath('//*[@id="inventory"]/div[2]/div/div[1]/div/div[1]/div[1]/a/h3/text()').getall())
        #print (response.css('h3::attr(class)').getall())
        #print (response.xpath('//h3//text()').getall()) # take a peek at the node-set

        cars = response.css('h3::text').getall()
        prices = response.css('strong::text').getall()

        car_data = [ ]
              
        for index, car in enumerate(cars):
            price =(prices[index].strip("$"))
            price = price.replace(',' , '')
            car_data.append((car + " " + price).split())
        
        count =index +1 # count the car data
        car_data = sorted(car_data)
        
        row = 1
        for car_line in car_data:
            col = 0
            for car_item in car_line:
                if (not car_item.isdigit()) and col>= 3: # if the item isn't numeric then skip it
                    continue
                self.data_out.set_cell(row, col+1, car_item, "Arial", False, 10 )
                col +=1
            row+=1

        self.data_out.set_cell(row+1, 1, ("Prices as of: " + self.date_time), "Arial", False, 10)
        print (self.dealer, "Total cars: " , count)
        self. data_out.save_file(self.file_out)

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()