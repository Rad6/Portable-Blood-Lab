
class Date:
    def __init__(self, year, month, day, hour):
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
    