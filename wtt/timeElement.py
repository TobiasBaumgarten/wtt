from enum import Enum, unique
import datetime

@unique
class timeType(Enum):
    workday = 1
    holiday = 2
    vecation = 3
    flexitime = 4
    spezialholiday = 5

class timeElement():
    def __init__(self, timeType: timeType, startDate: datetime, workingHours: datetime.timedelta = datetime.timedelta(hours=0)):
        self.timeType: timeType = timeType
        self.startDate: datetime = startDate
        self.workingHours: datetime.timedelta = workingHours

    @property
    def workingHours(self):
        return self._workingHours

    @workingHours.setter
    def workingHours(self, v: datetime.timedelta):
        if self.timeType == timeType.flexitime and v > datetime.timedelta(hours=0):
            raise ValueError("Flexitime cannot be positiv")
        self._workingHours = v

    def __add__(self, v):
        if isinstance(v, datetime.timedelta):
            return self.workingHours + v
        if isinstance(v, timeElement) or issubclass(v, timeElement):
            return self.workingHours + v.workingHours
