import json
import os

result = {"3102":{"weekdays": [], "sat": [], "sun": []}, "10-1": {"weekdays": [], "sat": [], "sun": []}}
string_3102_week = "05:30/05:50/06:05/06:20/06:40/07:00/07:20/07:40/08:00/08:40/09:20/10:00/10:30/11:00/11:20/11:40/12:00/12:20/12:50/13:20/13:50/14:20/14:50/15:20/15:40/16:00/16:20/16:45/17:10/17:35/18:00/18:30/19:00/19:30/19:50/20:10/20:40/21:15/21:50/22:30"
string_3102_sat = "05:40/06:10/06:35/06:50/07:20/08:00/08:40/09:20/10:00/10:40/11:20/12:00/12:40/13:20/14:00/14:40/15:20/16:00/16:35/17:15/17:55/18:35/19:15/19:55/20:30/21:10/21:50/22:30"
string_3102_sun = "05:40/06:15/06:50/07:25/08:05/08:45/09:30/10:15/11:00/11:45/12:40/13:25/14:10/14:55/15:40/16:30/17:15/18:00/18:45/19:30/20:10/20:55/21:45/22:30"
string_10_1_week = "06:30/07:00/07:30/08:00/08:25/08:50/09:15/09:40/10:05/10:30/11:20/12:00/12:50/13:20/13:45/14:10/14:40/15:05/15:35/16:00/16:50/17:30/18:20/18:45/19:15/19:40/20:10/20:35/21:00/21:35/22:30"

for x in string_3102_week.split("/"):
    result['3102']['weekdays'].append({"time": x})

for x in string_3102_sat.split("/"):
    result['3102']['sat'].append({"time": x})

for x in string_3102_sun.split("/"):
    result['3102']['sun'].append({"time": x})

for x in string_10_1_week.split("/"):
    result['10-1']['weekdays'].append({"time": x})
    result['10-1']['sat'].append({"time": x})
    result['10-1']['sun'].append({"time": x})

with open(f'{os.path.dirname(__file__)}/bus/timetable.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent='\t', ensure_ascii=False)
