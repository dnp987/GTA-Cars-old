# GTA-Cars
GTA Cars

This project was created to gather used car prices in the G.T.A (Greater Toronto Area) and display them in a web page. The page allows you to select a price range of used cars to display. The data is gathered by Selenium automation scripts written in Python. They go out to selected car dealers websites and gather used car data, such as year, make, model, price, inventory number, and a link back to the individual car on the dealer's website.

The data is stored in Execl spreadsheets, one per dealer. A python script reads each Excel spreadsheet and uploads the data to a MySQL database.

A MySQL database server allows the website to read car data and display it.
