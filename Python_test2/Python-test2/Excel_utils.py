'''
Created on May 6, 2020
Excel utilities to open, read, and write to excel files in .xlsx format

'''
import openpyxl
from openpyxl.worksheet import worksheet

class Excel_utils:

    def __init__(self, filename, sheet, in_out):
        self.filename = filename
        self.sheet = sheet
        self.in_out = in_out
        #self.wkbk = " "
        #self.sht = " "
                
    def set_worksheet(self):
        if (self.in_out == 'in'):
            self.wkbk = openpyxl.load_workbook(self.filename)
            #self.sht = self.wkbk.get_sheet_by_name(self.sheet)
            self.sht = self.wkbk[self.sheet]
        elif (self.in_out == 'out'):
            self.wkbk = openpyxl.Workbook()
            self.sht = self.wkbk.active
            self.sht.title = self.sheet
            
        # return wkbk, sht # Return the workbook and sheet objects
        #return self.sht # Return the sheet object