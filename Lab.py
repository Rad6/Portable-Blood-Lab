from BloodExpert import BloodExpert
from Test import Test
from LabPricingGate import LabPricingGate


class Lab: 
    def __init__(self, name, api_key, endpoint, blood_experts = [], tests = []):
        self.__name = name
        self.__api_key = api_key
        self.__endpoint = endpoint
        self.__blood_exeprts = blood_experts
        self.__tests = tests

    def getAvailableTimes(self):
        # TODO
        pass

    def getSupportedTests(self):
        # TODO
        pass

    def assignExpert(self, order):
        # TODO
        pass

    def getBloodExpers(self):
        return self.__blood_exeprts

    def calcPrice(self, detail):
        # TODO
        pass