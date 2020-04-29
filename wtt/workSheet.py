from typing import List
from wtt import timeElement
from datetime import *


class workSheet():
    timeElements = List[timeElement]

    def __init__(self):
        self.timeElements = []

    def append(self, timeElement: timeElement):
        self.timeElements.append(timeElement)

    def totalHours(self):
        result = timedelta(hours=0)
        for x in self.timeElements:
            result += x.workingHours
        return result

    def deltaHours(self, start: date, end: date):
        result = timedelta(hours=0)
        for x in self.timeElements:
            if x.startDate.date() >= start and x.startDate.date() <= end:
                result+= x.workingHours
        return result

    def addFlexi(self, datetime: datetime, flextimedelta: timedelta):
        if flextimedelta > timedelta(hours=0):
            raise ValueError("Flextime has to be negativ")
        self.append(timeElement(timeType.flexitime, datetime, flextimedelta))
