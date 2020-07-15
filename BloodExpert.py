from ServiceTime import ServiceTime
from DailySchedule import DailySchedule
from Location import Location
from ServiceTime import DateType
from datetime import datetime
from Date import Date

class BloodExpert:
    def __init__(self, id, location, daily_schedule = []):
        self.__id = id
        self.__location = location
        self.__daily_schedule = daily_schedule

    def getAvailableTimes(self):
        dss = self.getAllDailySchedule()
        available_times = []
        now = Date()
        now.setFromDateTime(datetime.today())
        for ds in dss:
            srvtimes = ds.getServiceTimes()
            for srvtime in srvtimes:
                avl = srvtime.getAccessibility()
                _type = srvtime.getType()
                if avl and (_type != DateType.special) and (now < srvtime.getDate()):
                    available_times.append(srvtime)
        return available_times

    def getDailySchedule(self, date):
        # TODO
        pass

    def getAllDailySchedule(self):
        return self.__daily_schedule
