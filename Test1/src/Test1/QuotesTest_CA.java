package Test1;
// Logs into BMO IL, verifies the home page, the main menu, then gets Canadian equity quotes

import excel_utils.*;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
import org.testng.annotations.AfterTest;
import org.testng.Assert;

import java.util.ArrayList;
import java.util.concurrent.TimeUnit;

public class QuotesTest_CA {
    public String baseURL = "";
    public String accNum = "";
    public String passWd = "";
    
     public WebDriver driver;
  
     @BeforeTest 
     public void setUp() {
           System.setProperty("webdriver.chrome.driver", "C:\\Selenium\\chromedriver.exe");
           driver = new ChromeDriver();
           
           Excel_utils data_sheet_in = new Excel_utils();
           data_sheet_in.setExcelFileSheet("c:\\temp\\test-parameters.xlsx", "test_parameters", "in");
          
           baseURL = data_sheet_in.getCell(1,1);
           accNum = data_sheet_in.getCell(2,1);
           passWd = data_sheet_in.getCell(3,1);

           driver.get(baseURL);
           driver.manage().timeouts().implicitlyWait(300, TimeUnit.SECONDS);
   	}
     
     @Test(priority =1)
     public void verifyHomePageTitle() {
          String expectedTitle = "BMO InvestorLine - Account Access";
          String actualTitle = driver.getTitle();
          System.out.println("Loading Log in page");
           Assert.assertEquals(actualTitle, expectedTitle);
     }
    
     @Test(priority = 2)
     public void verifyLogIn() {
         // Enter the account #, password, click on Sign in button
         WebElement login =  driver.findElement(By.id("loginText"));
         login.sendKeys(accNum);
         WebElement password = driver.findElement(By.name("password"));
         password.sendKeys(passWd);
         driver.findElement(By.id("sasi_btn")).click();
         WebDriverWait wait = new WebDriverWait(driver, 10);
         wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".home")));
         System.out.println("Loading home page");
     }

     @Test(priority = 3)
     public void verify_main_menu() {
    	 // Verify the main menu
    	 String[] expected_menu_items = {"Trading", "My Portfolio", "Quotes & Tools", "Markets & News"};
    	 String[] actual_menu_items = {"#nav_trading_main > a:nth-child(1)", "#nav_portfolio_main > a:nth-child(1)", "#nav_quotes_main > a:nth-child(1)","#nav_markets_main > a:nth-child(1)"};
    	 
    	  System.out.println("Checking main menu");
         for (int i=0; i < expected_menu_items.length; i++) {
        	 String actual_menu_found =  driver.findElement(By.cssSelector(actual_menu_items[i])).getText();
        	 Assert.assertEquals(actual_menu_found, expected_menu_items[i]);
         }
    }
     
     @Test(priority = 4)
     public void verify_quotes() {
    	 WebDriverWait wait = new WebDriverWait(driver, 60);   
    	 
         Excel_utils test_symbols = new Excel_utils();
         test_symbols.setExcelFileSheet("c:\\temp\\test1.xlsx", "symbols", "in");
         
 		Excel_utils data_sheet_out = new Excel_utils();
 		data_sheet_out.setExcelFileSheet( "", "Quotes", "out"); // create the data output spreadsheet
  	 
 		int startrow = test_symbols.startRow;
		int endrow = test_symbols.endRow;
		ArrayList<String> heading_data = new ArrayList<String>();
		heading_data.add("Symbol");
		heading_data.add("Last");
    	heading_data.add("Bid");
    	heading_data.add("Ask");
    	heading_data.add("High");
    	heading_data.add("Low");
    	heading_data.add("Open");
    	heading_data.add("Prev");
    	data_sheet_out.setCell(0, heading_data, "Arial", false, (short)10); // add the headings in row #0
    	
   	   String testSymbol = " "; 	 
    	     	 
    	 for (int i = startrow+1; i <= endrow; i++) {
    		 ArrayList<String> quote_data = new ArrayList<String>(); // reset the quote_data for each row
    		 testSymbol = test_symbols.getCell(i, 0);
    		 
    		 driver.findElement(By.cssSelector("#nav_quotes_main > a:nth-child(1)")).click(); // click on Quotes & Tools menu item
    	     wait.until(ExpectedConditions.elementToBeClickable(driver.findElement(By.cssSelector("div.paddingLeft25:nth-child(2) > input:nth-child(2)")))); //wait for symbol text box
    	     driver.findElement(By.cssSelector("div.paddingLeft25:nth-child(2) > input:nth-child(2)")).sendKeys(testSymbol, Keys.RETURN); // enter symbol and enter return to get a quote
    	      
    	     quote_data.add(testSymbol);
	    	 quote_data.add(driver.findElement(By.cssSelector(".brownContainer > div:nth-child(1) > span:nth-child(1)")).getAttribute("innerText")); // add last price
	    	 quote_data.add(driver.findElement(By.cssSelector("td.w16p:nth-child(2)")).getAttribute("innerText")); // add bid price
	    	 quote_data.add(driver.findElement(By.cssSelector("#table1 > table > tbody > tr:nth-child(2) > td:nth-child(2)")).getAttribute("innerText")); // add ask price
	    	 quote_data.add(driver.findElement(By.cssSelector("#table1 > table > tbody > tr.tableRowBG > td:nth-child(4)")).getAttribute("innerText")); // add high price
	    	 quote_data.add(driver.findElement(By.cssSelector("#table1 > table > tbody > tr:nth-child(2) > td:nth-child(4)")).getAttribute("innerText")); // add low price
	    	 quote_data.add(driver.findElement(By.cssSelector("#table1 > table > tbody > tr.tableRowBG > td:nth-child(6)")).getAttribute("innerText")); // add open price
	    	 quote_data.add(driver.findElement(By.cssSelector("#table1 > table > tbody > tr:nth-child(2) > td:nth-child(6)")).getAttribute("innerText")); // add prev price
    	     
	    	 data_sheet_out.setCell(i, quote_data, "rial", false, (short)10);
    	 }
    	 data_sheet_out.createDataOut("c:\\temp\\test3.xlsx"); 
     }
     
     @AfterTest
     public void endSession() {
    	driver.quit();
     }
}