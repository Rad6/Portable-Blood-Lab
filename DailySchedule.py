from Date import Date
from ServiceTime import ServiceTime


class DailySchedule:
    def __init__(self, date, service_times = []):
        self.__date = date
        self.__service_times = service_times

    def getServiceTimes(self):
        return self.__service_times

    def getServiceTime(self, date):
        # TODO
        pass
