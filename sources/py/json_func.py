import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from config import *

def load(id):
    with codecs.open(scheduleFilePath[str(id)], encoding='utf-8') as schedule_file:
        #Сохраняем расписание в виде словаря Python
        schedule = json.loads(schedule_file.read())
    return schedule
    
def save(schedule, id):
    with codecs.open(scheduleFilePath[str(id)], "w", encoding='utf-8') as schedule_wfile:
        json.dump(schedule, schedule_wfile)

def countin(schedule):
    count = 0
    
    for subject in schedule:
        count = count + 1
        
    return count

def getday(date):
    return int(date[0][:2])
    
def getmonth(date):
    return int(date[0][3:5])

def comparedates(date1, date2): #if date1 >= date2 return True
    if getmonth(date1) > getmonth(date2):
        return True
    elif getmonth(date1) < getmonth(date2):
        return False
    elif getday(date1) > getday(date2):
        return True
    elif getday(date1) < getday(date2):
        return False
    elif date1[1] > date2[1]:
        return True
    else:
        return False

def timesort(schedule):

    count = countin(schedule['VCALENDAR'][0]['VEVENT'])

    for i in range(count - 1):
        imindate = i
        
        for j in range(i + 1, count):
            if comparedates(get_date_and_time(schedule['VCALENDAR'][0]['VEVENT'][imindate]), get_date_and_time(schedule['VCALENDAR'][0]['VEVENT'][j])):
                imindate = j
        
        if i != imindate:
            bkp = schedule['VCALENDAR'][0]['VEVENT'][imindate]
            schedule['VCALENDAR'][0]['VEVENT'][imindate] = schedule['VCALENDAR'][0]['VEVENT'][i]
            schedule['VCALENDAR'][0]['VEVENT'][i] = bkp
    
    #for i in range(count - 1):
    #    print(comparedates(get_date_and_time(schedule['VCALENDAR'][0]['VEVENT'][i]), get_date_and_time(schedule['VCALENDAR'][0]['VEVENT'][i + 1])))
    
    return schedule

    #//for subject in schedule['VCALENDAR'][0]['VEVENT']:
    #    time = subject['
    
def sorting(id):
    save(timesort(load(id)), id)
    
