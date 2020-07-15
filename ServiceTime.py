from Date import Date
from enum import Enum


class DateType(Enum):
    ordinary = 1
    special = 2
    

class ServiceTime:
    def __init__(self, date, accessibility=True, type=DateType.ordinary):
        self.__date = date
        self.__accessibility = accessibility
        self.__type = type

    def getDate(self):
        return self.__date

    def setDate(self, value):
        self.__date = value

    def getAccessibility(self):
        return self.__accessibility

    def setAccessibility(self, value):
        self.__accessibility = value

    def getType(self):
        return self.__type

    def setType(self, value):
        self.__type = value
    
    def __str__(self):
        return f"ServiceTime:(at {str(self.__date)}, acc:{self.__accessibility}, type={self.__type})"