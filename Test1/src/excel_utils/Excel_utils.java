package excel_utils;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;


import org.apache.poi.xssf.usermodel.XSSFCell;
import org.apache.poi.xssf.usermodel.XSSFCellStyle;
import org.apache.poi.xssf.usermodel.XSSFFont;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.DataFormatter;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.ss.util.CellUtil;


public class Excel_utils {

	// Excel workbook
	private  XSSFWorkbook wb_in;
	private  XSSFWorkbook wb_out;

	// Excel sheet
	private  XSSFSheet sht_in;
	private  XSSFSheet sht_out;
	// Excel cell
	private  XSSFCell cell;
	
	// Excel row
	private  XSSFRow row; 
	
	// Starting row
	public int startRow;
	
	// Ending row
	public int endRow;
	
	public void setExcelFileSheet(String fileName, String sheetName, String inOut) { // set the excel sheet to be used
		//System.out.println("setExcelFileSheet");
		try {
			switch ( inOut ) {
			case "in": // create input file stream, workbook, and sheet
				FileInputStream fileIn = new FileInputStream(fileName);
				wb_in = new XSSFWorkbook(fileIn);
				sht_in =  wb_in.getSheet(sheetName);
				startRow = sht_in.getFirstRowNum();
				endRow = sht_in.getLastRowNum();
				
			case "out": // create output workbook and sheet
				wb_out = new XSSFWorkbook();
				sht_out =  wb_out.createSheet("Quotes");
			}
		}
		catch (IOException e1) {
				e1.printStackTrace();
			}
		}
	
	public String getCell(int row_num, int col_num) { // get the cell data from the excel sheet
		//System.out.println("getCell");
		String cell_data;
		DataFormatter formatter = new DataFormatter();
		cell = sht_in.getRow(row_num).getCell(col_num);
		cell_data = formatter.formatCellValue(cell) ;
		return cell_data;
	}
	
	public void setCell(int row_num, ArrayList<String> data, String font_name, boolean bold_font,  short font_size) { //set the cell data
		//System.out.println("setCell");
		XSSFFont font = wb_out.createFont();
		XSSFCellStyle style = wb_out.createCellStyle();
		row = sht_out.createRow(row_num);
		font.setFontName(font_name);
		font.setFontHeightInPoints(font_size);
		
		if (bold_font) { // if flag for bold font is on, set it
			font.setBold(true);
		}
		style.setFont(font);
		
		for (int i = 0; i < data.size(); i++) {
			CellUtil.createCell(row, i, data.get(i), style);
		}
	}
	
	public void createDataOut(String file_name) {
		//System.out.println("createDataOut");
		try {
			FileOutputStream fileOut = new FileOutputStream(file_name); 
			wb_out.write(fileOut);
			fileOut.flush();
			fileOut.close();
		}
		catch (IOException e1) {
			e1.printStackTrace();
		}
	}
}