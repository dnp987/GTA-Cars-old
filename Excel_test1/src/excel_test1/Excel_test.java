package excel_test1;

import java.io.File;
import java.io.FileInputStream;
import java.util.Iterator;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;


public class Excel_test {
		static XSSFRow row;
		
		public static void main(String [] args)  throws Exception {
			System.out.println("Excel_test");
			 FileInputStream file = new FileInputStream(new File("c:\\temp\\test1.xlsx"));
			 XSSFWorkbook wb = new XSSFWorkbook(file);
			 XSSFSheet sht = wb.getSheetAt(0);
			 
			 Iterator <Row> rowIterator = sht.iterator();
			 
			 while (rowIterator.hasNext()) {
				row = (XSSFRow) rowIterator.next();
				Iterator <Cell>  cellIterator = row.cellIterator();
				
				while ( cellIterator.hasNext()) {
		            Cell cell = cellIterator.next();
		            
		            switch (cell.getCellType()) {
		               case NUMERIC:
		                  System.out.print(cell.getNumericCellValue() + "\t");
		                  break;
               
		               case STRING:
		                  System.out.print(cell.getStringCellValue() + "\t");
		                  break;
		            }
		         }
		         System.out.println();
			 }
			wb.close();
			file.close();
		}
	}