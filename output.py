import openpyxl
import time


def dealDate(companyName_set,companyPid_set):
    current_datetime = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = current_datetime + "_file.xlsx"
    workbook = openpyxl.Workbook()
    sheet1 = workbook.active
    sheet1['A1'] = "控股公司"
    sheet1['B1'] = "PID"
    nameColumn = 1
    pidColumn = 2
    for row_index,value1 in enumerate(companyName_set,start=2):
        sheet1.cell(row=row_index,column=nameColumn).value = value1
    for row_index,value2 in enumerate(companyPid_set,start=2):
        sheet1.cell(row=row_index,column=pidColumn).value = value2

    workbook.save(file_name)