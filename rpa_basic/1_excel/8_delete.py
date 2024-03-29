from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.delete_rows(8)
# ws.delete_rows(8, 3) # 8번재 줄부터 총 3줄 삭제
# wb.save("sample_delete_rows.xlsx")

ws.delete_cols(2)   # 2번째 열 (B) 삭제
ws.delete_cols(2, 2)    # 2번째 열로부터 총 2개 열 삭제

wb.save("sample_delete_col.xlsx")