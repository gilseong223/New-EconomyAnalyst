from openpyxl import load_workbook

# data_only=Ture로 해줘야 수식이 아닌 값으로 받아온다.
load_wb = load_workbook("상장법인목록.xlsx", data_only=True)
# 시트 이름으로 불러오기
load_ws = load_wb['상장법인목록']

print('\n-----모든 행 단위로 출력-----')
for row in load_ws.rows:
    tmp = True
    for cell in row:
        if cell.value=='롯데정보통신':
            tmp = False
            print(cell.value)
        elif not tmp :
            name = str(int(cell.value))
            name_len = len(name)
            tmp_name = ''
            for i in range(6-name_len):
                tmp_name += '0'
            tmp_name += name
            print(tmp_name)
            break
        else :
            break