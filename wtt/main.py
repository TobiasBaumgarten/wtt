""" from workTime import *
from datetime import *
from workSheet import workSheet
from timeElement import timeElement, timeType

a = workTime(datetime(2020,4,1,7),endDate=datetime(2020,4,1,15))
b = workTime(datetime(2020,4,2,8),endDate=datetime(2020,4,2,15))
ws = workSheet()
ws.append(a)
ws.append(b)
ws.addFlexi(datetime(2020,4,3),timedelta(hours=-3))

print(ws.deltaHours(date(2020,4,1), date(2020,4,2)))
print(ws.totalHours()) """

#TODO Unittest

import wwt.wwt.main
