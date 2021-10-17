package excel_test1;

import java.io.File;
import java.io.FileInputStream;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class Excel_test2 {
		static XSSFRow row;
		
		public static void main(String [] args)  throws Exception {
			System.out.println("Excel_test2");
			FileInputStream file = new FileInputStream(new File("c:\\temp\\test1.xlsx"));
			XSSFWorkbook wb = new XSSFWorkbook(file);
			XSSFSheet sht = wb.getSheet("TestDataIn");
			int i=0;
			
			for (Row row : sht) {
				for (Cell cell: row) {
					i++;
					if (i == 1) { // skip the first row of the spreadsheet, it contains headings
						continue;
					}
						
			        switch (cell.getCellType()) {
			              case NUMERIC:
			                  System.out.print(cell.getNumericCellValue() + "\n");
			                  break;
		               
			               case STRING:
			                  System.out.print(cell.getStringCellValue() + "\n");
			                  break;
			            }	
					}
			}
			    System.out.println();
				wb.close();
				file.close();
		 }
}