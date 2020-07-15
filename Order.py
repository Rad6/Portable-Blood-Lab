
class Order:
    def __init__(self):

        self.__presc_detail = None
        self.__status = None
        self.__is_canceled = None
        self.__tracking_code = None
        self.__labs_tracking_code = None
        self.__fault_code = None
        self.__price = None
        self.__address = None
        self.__lab = None
        self.__blood_expert = None
        self.__payment_detail = None
        self.__user = None
        self.__service_time = None
        self.__test_list = None

    
    def getPrescDetail(self):
        return self.__presc_detail
    
    def setPrescDetail(self, value):
        self.__presc_detail = value

    def getLab(self):
        return self.__lab

    def setLab(self, value):
        self.__lab = value

    def setServiceTime(self, value):
        self.__service_time = value

    def getServiceTime(self):
        return self.__service_time

    def chooseTests(self, tests = []):
        # TODO
        pass

    def createTestList(self):
        # TODO
        pass

    def getFinalLabs(self):
        # TODO
        pass

    def setStatus(self, value):
        self.__status = value

    def getPrice(self):
        return self.__price

    def setPrice(self, value):
        self.__price = value

    def getTestList(self):
        return self.__test_list

    def calcTotalPrice(self, price):
        # TODO
        pass

    def doPayment(self):
        # TODO
        pass

    def setBloodExpert(self, value):
        self.__blood_expert = value

    
