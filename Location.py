
class Location:
    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude
    
    def __str__(self):
        return f"Location({self.__latitude}, {self.__longitude})"