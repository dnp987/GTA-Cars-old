package excel_test1;
import java.io.IOException;
import java.util.ArrayList;

import excel_utils.*;

public class Excel_test4 {

	public static void main(String[] args) throws IOException {
		String symbol = "";
				
		System.out.println("Running ..." + "Excel_test4\n");
		Excel_utils data_sheet_in = new Excel_utils();
		data_sheet_in.setExcelFileSheet("c:\\temp\\test1.xlsx", "symbols", "in");
		int startrow = data_sheet_in.startRow;
		int endrow = data_sheet_in.endRow;
				
		for (int i = startrow +1; i <= endrow; i++) { // skip the 1sr row, it's for headings
			symbol = data_sheet_in.getCell(i,0);
			System.out.println(symbol);
		}
		Excel_utils data_sheet_out = new Excel_utils();
		data_sheet_out.setExcelFileSheet( "", "Quotes", "out"); // create the data output spreadsheet
		ArrayList<String> quote_data = new ArrayList<String>();
		quote_data.add("65.5");
		quote_data.add("45.67");
		quote_data.add("99.99");
		quote_data.add("199.99");
		quote_data.add("299.99");
		
		data_sheet_out.setCell(0, quote_data, "Arial", true, (short)12);
		data_sheet_out.setCell(1, quote_data, "Verdana", false, (short)10);
		data_sheet_out.setCell(2, quote_data, "Courier", false, (short)10);
		
		data_sheet_out.createDataOut( "c:\\temp\\test3.xlsx");
		
		data_sheet_in.setExcelFileSheet("c:\\temp\\test1.xlsx", "test_parameters", "in");
		startrow = data_sheet_in.startRow;
		endrow = data_sheet_in.endRow;
		
		for (int i = startrow +1; i <= endrow; i++) { // skip the 1st row, it's for headings
			symbol = data_sheet_in.getCell(i,1);
			System.out.println(symbol);
		}
		
	}	
}