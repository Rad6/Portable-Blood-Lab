from Test import Test

class TestList:
    def __init__(self, tests=[]):
        self.__tests = tests
    
    def setTests(self, tests):
        self.__tests = tests
    
    def getTests(self):
        return self.__tests

    def __str__(self):
        _str = "Testlist:"
        for test in self.getTests():
            _str += "\n" + str(test)
        return _str