from openpyxl import load_workbook

# clears the comp excel workbook
# keeps the first sheet because excel requires at least 1 sheet in each workbook
def clearExcel(excelName):
    wb = load_workbook(filename = excelName)
    sheetList = wb.get_sheet_names()
    firstSheet = True
    for sheet in sheetList:
        if firstSheet == True:
            firstSheet = False
            continue
        std = wb.get_sheet_by_name(sheet)
        wb.remove_sheet(std)
    wb.save(filename = excelName)

def main():
    excelName = "comps.xlsx"
    clearExcel(excelName)

main()