import openpyxl, json

workbook = openpyxl.load_workbook('C:\\Users\\Roadtech\\Downloads\\수인분당선 시간표(2020년 11월1일)수정.xlsx', read_only=True, data_only=True)
result = {"weekdays":{"up":[], "down":[]}, "weekend":{"up":[], "down":[]}}

worksheet = workbook['평일(상행)']
row_index = 1

for row in worksheet.rows:
    if row_index > 2:
        if row[openpyxl.utils.column_index_from_string("D") - 1].value:
            if row[openpyxl.utils.column_index_from_string("Z") - 1].value:
                result['weekdays']['up'].append({"endStn":  row[openpyxl.utils.column_index_from_string("C") - 1].value, "time": str(row[openpyxl.utils.column_index_from_string("Z") - 1].value)})
        else:
            break
    row_index += 1

worksheet = workbook['평일(하행)']
row_index = 1

for row in worksheet.rows:
    if row_index > 2:
        if row[openpyxl.utils.column_index_from_string("D") - 1].value:
            if row[openpyxl.utils.column_index_from_string("AV") - 1].value:
                result['weekdays']['down'].append({"endStn":  row[openpyxl.utils.column_index_from_string("C") - 1].value, "time": str(row[openpyxl.utils.column_index_from_string("AV") - 1].value)})
        else:
            break
    row_index += 1

worksheet = workbook['휴일(상행)']
row_index = 1

for row in worksheet.rows:
    if row_index > 2:
        if row[openpyxl.utils.column_index_from_string("D") - 1].value:
            if row[openpyxl.utils.column_index_from_string("Y") - 1].value:
                result['weekend']['up'].append({"endStn":  row[openpyxl.utils.column_index_from_string("C") - 1].value, "time": str(row[openpyxl.utils.column_index_from_string("Y") - 1].value)})
        else:
            break
    row_index += 1

worksheet = workbook['휴일(하행)']
row_index = 1

for row in worksheet.rows:
    if row_index > 2:
        if row[openpyxl.utils.column_index_from_string("D") - 1].value:
            if row[openpyxl.utils.column_index_from_string("AU") - 1].value:
                result['weekend']['down'].append({"endStn":  row[openpyxl.utils.column_index_from_string("C") - 1].value, "time":str(row[openpyxl.utils.column_index_from_string("AU") - 1].value)})
        else:
            break
    row_index += 1

with open('subway/suinline.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent='\t', ensure_ascii=False)