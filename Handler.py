# from Lab import Lab
# from ServiceTime import ServiceTime
from filler import generateSampleOrder

class Handler:
    def __init__(self):
        self.__order = None

    def enterPrescriptionID(self, pid):
        pass
    
    def createTests(self):
        pass

    def getTests(self):
        pass

    def chooseTests(self, tests):
        pass

    def getTimes(self):
        self.__order = generateSampleOrder() # TODO: JUST A SAMPLE ORDER ~~~~~~~~~~ DELETE IT IN FUTURE ~~~~~~~~~~~~~~~~~~~~``
        lab = self.__order.getLab()
        totaltimes = lab.getAvailableTimes()
        return totaltimes

    def chooseTime(self, service_time):
        service_time.setAccessibility(False)
        self.__order.setServiceTime(service_time)
        print(f"the chosen time is: {str(self.__order.getServiceTime())}")
    
    def getLabs(self):
        pass
    
    def chooseLab(self, lab):
        pass

    def enterAddress(self, address):
        pass

    def enterFaultCode(self, fault_code):
        pass

    def startNewOrder(self):
        pass

    def payOnline(self):
        pass

    def getOrder(self):
        return self.__order

    def setOrder(self, order):
        self.__order = order