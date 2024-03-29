from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8)   # 8번째 줄이 비워지
# ws.insert_rows(8, 5)    # 8번째 줄 위치에 5줄을 추가

ws.insert_cols(2)
ws.insert_cols(2, 3)
wb.save("sample_insert_rows.xlsx")



# wb.save("sample_insert_rows.xlsx")
