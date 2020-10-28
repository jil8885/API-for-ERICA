import openpyxl, json

workbook = openpyxl.load_workbook('C:\\Users\\Jeongin\\Downloads\\수인분당선 시간표(2020년9월12일)0910.xlsx', read_only=True, data_only=True)
result = {"weekdays":{"up":[], "down":[]}, "weekend":{"up":[], "down":[]}}

worksheet = workbook['평일(상)']

for index, row in enumerate(worksheet.rows):
    if index > 1:
        if row[openpyxl.utils.column_index_from_string("D") - 1].value:
            if row[openpyxl.utils.column_index_from_string("Z") - 1].value:
                result['weekdays']['up'].append({"endStn":  row[openpyxl.utils.column_index_from_string("C") - 1].value, "time": str(row[openpyxl.utils.column_index_from_string("Z") - 1].value)})
        else:
            break

worksheet = workbook['평일(하)']

for index, row in enumerate(worksheet.rows):
    if index > 1:
        if row[openpyxl.utils.column_index_from_string("D") - 1].value:
            if row[openpyxl.utils.column_index_from_string("AV") - 1].value:
                result['weekdays']['down'].append({"endStn":  row[openpyxl.utils.column_index_from_string("C") - 1].value, "time": str(row[openpyxl.utils.column_index_from_string("AV") - 1].value)})
        else:
            break

worksheet = workbook['휴일(상)']

for index, row in enumerate(worksheet.rows):
    if index > 1:
        if row[openpyxl.utils.column_index_from_string("D") - 1].value:
            if row[openpyxl.utils.column_index_from_string("Y") - 1].value:
                result['weekend']['up'].append({"endStn":  row[openpyxl.utils.column_index_from_string("C") - 1].value, "time": str(row[openpyxl.utils.column_index_from_string("Y") - 1].value)})
        else:
            break

worksheet = workbook['휴일(하)']

for index, row in enumerate(worksheet.rows):
    if index > 1:
        if row[openpyxl.utils.column_index_from_string("D") - 1].value:
            if row[openpyxl.utils.column_index_from_string("AU") - 1].value:
                result['weekend']['down'].append({"endStn":  row[openpyxl.utils.column_index_from_string("C") - 1].value, "time":str(row[openpyxl.utils.column_index_from_string("AU") - 1].value)})
        else:
            break
    row_index += 1

with open('subway/suinline.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent='\t', ensure_ascii=False)
