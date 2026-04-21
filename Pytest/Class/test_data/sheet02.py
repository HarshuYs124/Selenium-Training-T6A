import openpyxl

def get_test_data():
    wb=openpyxl.load_workbook(r'/Class/Pytest/2-Apr\sample.xlsx')
    ws = wb["sheet1"]

    data = []
    for row in ws.iter_rows(min_row =2,values_only=True):  # to iterate in sheet
        data.append(row)
    return data