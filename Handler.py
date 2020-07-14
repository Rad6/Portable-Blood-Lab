from Order import Order

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
        return None

    def chooseTime(self, service_time):
        pass
    
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