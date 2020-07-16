from datetime import datetime

class Date:
    def __init__(self, year=0, month=0, day=0, hour=0):
        self.__year = year
        self.__month = month
        self.__day = day
        self.__hour = hour

    def getYear(self):
        return self.__year
    def setYear(self, value):
        self.__year = value
    
    def getMonth(self):
        return self.__month
    def setMonth(self, value):
        self.__month = value
    
    def getDay(self):
        return self.__day
    def setDay(self, value):
        self.__day = value
    
    def getHour(self):
        return self.__hour
    def setHour(self, value):
        self.__hour = value
    
    def setFromDateTime(self, dt):
        self.setYear(dt.year)
        self.setMonth(dt.month)
        self.setDay(dt.day)
        self.setHour(dt.hour)

    def __gt__(self, other):
        if self.getYear() > other.getYear():
            return True
        if self.getMonth() > other.getMonth() and self.getYear() == other.getYear():
            return True
        if self.getDay() > other.getDay() and\
             self.getYear() == other.getYear() and self.getMonth() == other.getMonth():
            return True
        if self.getHour() > other.getHour() and\
            self.getYear() == other.getYear() and self.getMonth() == other.getMonth() and\
                self.getDay() == other.getDay():
            return True
        return False

    def __eq__(self, other):
        if self.getYear() == other.getYear() and self.getMonth() == other.getMonth() and\
                self.getDay() == other.getDay() and self.getHour() == other.getHour():
            return True
        return False
    
    def __str__(self):
        return f"Date({self.__year}.{self.__month}.{self.__day} at {self.__hour})"