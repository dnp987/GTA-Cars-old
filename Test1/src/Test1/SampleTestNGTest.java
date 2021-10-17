package Test1;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
import org.testng.Assert;
import java.util.concurrent.TimeUnit;

public class SampleTestNGTest {

     public String baseUrl = "https://google.com/";
     public WebDriver driver;
  

     @BeforeTest

     public void setBaseUrl() {

           System.setProperty("webdriver.chrome.driver", "C:\\Selenium\\chromedriver.exe");
           driver = new ChromeDriver();
           driver.get(baseUrl);
           driver.manage().timeouts().implicitlyWait(300, TimeUnit.SECONDS);
     }

     @Test

     public void verifyHomePageTitle() {

           String expectedTitle = "Google";
           String actualTitle = driver.getTitle();
           System.out.println("The actual title is: " + actualTitle);
           Assert.assertEquals(actualTitle, expectedTitle);

     }
    
     @AfterTest

     public void endSession() {
     driver.quit();

     }
}
