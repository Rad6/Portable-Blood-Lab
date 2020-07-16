from ServiceTime import ServiceTime
from DailySchedule import DailySchedule
from Location import Location
from ServiceTime import DateType
from datetime import datetime
from Date import Date
from Person import Person

class BloodExpert(Person):
    def __init__(self, id, location=(0, 0), daily_schedule = []):
        self.__id = id
        self.__location = location
        self.__daily_schedule = daily_schedule
        super().__init__()

    def getAvailableTimes(self, with_faultcode=False):
        dss = self.getAllDailySchedule()
        available_times = []
        now = Date()
        now.setFromDateTime(datetime.today())
        for ds in dss:
            srvtimes = ds.getServiceTimes()
            for srvtime in srvtimes:
                avl = srvtime.getAccessibility()
                _type = srvtime.getType()
                if avl and ((_type != DateType.special) or with_faultcode) and \
                    (now < srvtime.getDate()):
                    available_times.append(srvtime)
        return available_times

    def getDailySchedule(self, date):
        for each in self.__daily_schedule:
            if (each.getDate().getYear() == date.getYear()) and \
                (each.getDate().getMonth() == date.getMonth()) and \
                    (each.getDate().getDay() == date.getDay()):
                return each
        return -1        

    def getAllDailySchedule(self):
        return self.__daily_schedule

    def getID(self):
        return self.__id
