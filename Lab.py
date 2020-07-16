from BloodExpert import BloodExpert
from Test import Test
from LabPricingGate import LabPricingGate

from Location import Location
from DailySchedule import DailySchedule
from Date import Date
from ServiceTime import ServiceTime, DateType

class Lab: 
    def __init__(self, name, api_key="dflk2904jf094", \
        endpoint="https://lab.com/price", blood_experts = [], tests = []):
        self.__name = name
        self.__api_key = api_key
        self.__endpoint = endpoint
        self.__blood_exeprts = blood_experts
        self.__tests = tests

    def getAvailableTimes(self):
        bldexperts = self.getBloodExperts()
        totaltimes = []
        for item in bldexperts:
            srvtime = item.getAvailableTimes()
            for item in srvtime:
                totaltimes.append(item)
        return totaltimes

    def getSupportedTests(self):
        # TODO: Kiarash: Farghesh ba getTests chie?
        #       Hadi: Hechi :D
        pass
    
    def getTests(self):
        return self.__tests

    def setTests(self, tests):
        self.__tests = tests
    
    def assignExpert(self, order):
        blood_experts = self.getBloodExperts()
        order_date = order.getServiceTime().getDate()
        for each in blood_experts:
            daily_schedule = each.getDailySchedule(order_date)
            if daily_schedule == -1:
                continue
            service_time = daily_schedule.getServiceTime(order_date)
            if service_time == -1:
                continue
            availability = service_time.getAccessibility()
            if availability:
                each.getDailySchedule(order_date).getServiceTime(order_date).setAccessibility(False)
                order.setBloodExpert(each)
                break

    def setBloodExperts(self, blood_experts):
        self.__blood_exeprts = blood_experts
    
    def getBloodExperts(self):
        return self.__blood_exeprts

    def getAPIKey(self):
        return self.__api_key

    def getEndPoint(self):
        return self.__endpoint

    def calcPrice(self, detail):
        apikey = self.getAPIKey()
        endpoint = self.getEndPoint()
        price = LabPricingGate.getPrice(detail, apikey, endpoint)
        return price

    def getName(self):
        return self.__name