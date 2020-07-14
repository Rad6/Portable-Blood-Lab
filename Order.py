
class Order:
    def __init__(self, presc_detail, status, is_canceled, tracking_code, labs_tracking_code, fault_code, 
                price, address, lab, blood_expert, payment_detail, user, service_time, test_list):

        self.__presc_detail = presc_detail
        self.__status = status
        self.__is_canceled = is_canceled
        self.__tracking_code = tracking_code
        self.__labs_tracking_code = labs_tracking_code
        self.__fault_code = fault_code
        self.__price = price
        self.__address = address
        self.__lab = lab
        self.__blood_expert = blood_expert
        self.__payment_detail = payment_detail
        self.__user = user
        self.__service_time = service_time
        self.__test_list = test_list

    
    def getPrescDetail(self):
        return self.__presc_detail
    
    def setPrescDetail(self, value):
        self.__presc_detail = value

    def getLab(self):
        return self.__lab

    def setLan(self, value):
        self.__lab = value

    def setServiceTime(self, value):
        self.__service_time = value

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

    
