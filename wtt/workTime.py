from datetime import *
from .timeElement import timeElement, timeType


class workTime(timeElement):
    """ 
    Constans
    """
    _endDate: datetime
    __pause: timedelta
    __DEFAULT_WORKINGHOURS = timedelta(hours=8)
    __DEFAULT_PAUSE = timedelta(minutes=0)
    __MIN_WORKINGHOURS = timedelta(seconds=0)
    __MAX_WORKINGHOURS = timedelta(hours=24)

    def __init__(self, startDate: datetime, pause: timedelta = __DEFAULT_PAUSE, endDate: datetime = None):
        super().__init__(timeType.workday, startDate)
        self.pause: timedelta = pause
        self.endDate: datetime = endDate

    def isendDateSet(self):
        return self._endDate != None

    @property
    def endDate(self):
        if self._endDate == None:
            return self.startDate + self.pause
        return self._endDate

    @endDate.setter
    def endDate(self, v: datetime):
        if v == None:
            self._endDate = v
            return
        if v.date() != self.startDate.date():
            raise ValueError(
                "The endDate must be on the same day as the startDate")
        if v + self.pause < self.startDate:
            raise ValueError(
                f"The endDate ({v}) time has to be later then the startDate ({self.startDate}) time")
        self._endDate = v

    @property
    def workingHours(self):
        return self.endDate - self.startDate - self.pause

    @workingHours.setter
    def workingHours(self, v: timedelta):
        if v >= self.__MIN_WORKINGHOURS and v <= self.__MAX_WORKINGHOURS:
            self.setDeltaToday(v)
        else:
            raise ValueError

    @property
    def pause(self):
        return self.__pause

    @pause.setter
    def pause(self, v: timedelta):
        if v <= self.__MAX_WORKINGHOURS:  # TODO: More Error cases.
            self.__pause = v
        else:
            raise ValueError

    def setDeltaToday(self, workhours: timedelta):
        a = workTime.setDeltaToday(workhours)
        self.startDate = a.startDate
        self.endDate = a.endDate
        self.pause = a.pause

    @staticmethod
    def setDeltaToday(workhours: timedelta, start=7, pause: timedelta = timedelta(minutes=30)):
        a = datetime.today()
        if start < 0 or start > 24:
            raise ValueError("startDate has be bigger than 0 or less than 24")
        start = datetime(a.year, a.month, a.day, start)
        return workTime.setDelta(start, workhours, pause)

    @staticmethod
    def setDelta(date: datetime, workhours: timedelta, pause: timedelta = timedelta(minutes=30)):
        return workTime(date, pause, date+workhours+pause)

    def __repr__(self):
        return f'hours: {self.workingHours}, start: {self.startDate}, end: {self.endDate}, pause: {self.pause}'
