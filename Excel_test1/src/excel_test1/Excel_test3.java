package excel_test1;

import java.io.File;
import java.io.FileInputStream;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class Excel_test3 {
		
	public static void main(String [] args)  throws Exception {
		System.out.println("Excel_test3");
		FileInputStream file = new FileInputStream(new File("c:\\temp\\test1.xlsx"));
		XSSFWorkbook wb = new XSSFWorkbook(file);
		XSSFSheet sht = wb.getSheet("TestDataIn");
		int startrow = sht.getFirstRowNum();
		int endrow = sht.getLastRowNum();
		String symbol = "";

		for ( int i = startrow+1; i <= endrow; i++  ) {
			symbol = sht.getRow(i).getCell(0).toString();
			System.out.println(i + " " + symbol);
		}
			wb.close();
			file.close();
	}
}