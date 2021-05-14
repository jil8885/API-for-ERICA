import openpyxl
import json

from openpyxl.utils import column_index_from_string


def dump_timetable():
    workbook = openpyxl.load_workbook('C:\\Users\\Jeongin\\Downloads\\수인분당선.xlsx', read_only=True, data_only=True)
    result = {"weekdays": {"up": [], "down": []}, "weekend": {"up": [], "down": []}}

    heading_column = "C"
    worksheet_information = [("평일상행", "Z", "weekdays", "up"), ("평일하행", "AW", "weekdays", "down"),
                             ("휴일상행", "Y", "weekend", "up"), ("평일하행", "AU", "weekend", "down")]

    for sheet, column, key1, key2 in worksheet_information:
        worksheet = workbook[sheet]

        for row_index, row in enumerate(worksheet.rows):
            if row_index > 2:
                if row[column_index_from_string(column) - 1].value and str(row[column_index_from_string(column) - 1].value).strip():
                    result[key1][key2].append({"endStn": row[column_index_from_string(heading_column) - 1].value,
                                               "time": str(row[column_index_from_string(column) - 1].value)})

    with open('subway/suinline.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent='\t', ensure_ascii=False)

dump_timetable()
