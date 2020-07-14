from Date import Date
from ServiceTime import ServiceTime


class DailySchedule:
    def __init__(self, date, service_time = []):
        self.__date = date
        self.__service_time = service_time

    def getServiceTimes(self):
        return self.__service_time

    def getServiceTime(self, date):
        # TODO
        pass
