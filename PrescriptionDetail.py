from Test import Test

class PrescriptionDetail:
    def __init__(self, prescID="no-id", isCovered=False, \
        isAccepted=False, tests=[]):
        self.__prescID = prescID
        self.__isAccepted = isAccepted
        self.__isCovered = isCovered
        self.__tests = tests

    def getPrescID(self):
        return self.__prescID
    
    def setPrescID(self, prescID):
        self.__prescID = prescID
    
    def getIsAccepted(self):
        return self.__isAccepted
    
    def setIsAccepted(self, isAccepted):
        self.__isAccepted = isAccepted

    def setIsCovered(self, isCovered):
        self.__isCovered = isCovered

    def getIsCovered(self):
        return self.__isCovered
    
    def getTests(self):
        return self.__tests

    def setTests(self, tests):
        self.__tests = tests

    def __str__(self):
        _str = "\nPrescriptionDetail:"
        _str += f"\n\tprescid: {self.getPrescID()}"
        _str += f"\n\tisCovered: {self.getIsCovered()}"
        _str += f"\n\tisAccepted: {self.getIsAccepted()}"
        _str += f"\n\tTests:"
        for test in self.getTests():
            _str += f"\n\t\t{str(test)}"
        return _str