
class Person:
    def __init__(self, name="no-name", lastname="no-last", \
        snn="0000000000", sex="transgender", email="null@gamil.com", phone="9092301202"):
        self.__name = name
        self.__lastname = lastname
        self.__snn = snn
        self.__sex = sex
        self.__email = email
        self.__phone = phone
    
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getLastname(self):
        return self.__lastname

    def setLastname(self, lastname):
        self.__lastname = lastname

    def getSnn(self):
        return self.__snn

    def setSnn(self, snn):
        self.__snn = snn

    def getSex(self):
        return self.__sex

    def setSex(self, sex):
        self.__sex = sex

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone
    
    def __str__(self):
        return f"name: {self.__name}, lastname: {self.__lastname}"