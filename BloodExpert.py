from ServiceTime import ServiceTime
from DailySchedule import DailySchedule
from Location import Location


class BloodExpert:
    def __init__(self, id, location, daily_schedule = []):
        self.__id = id
        self.__location = location
        self.__daily_schedule = daily_schedule

    def getAvailableTime(self):
        # TODO
        pass

    def getDailySchedule(self, date):
        # TODO
        pass

    def getAllDailySchedule(self):
        return self.__daily_schedule
