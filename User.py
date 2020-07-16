from Prescription import Prescription
from Person import Person
from Order import Order

class User(Person):
    def __init__(self, username, is_logged_in=False, \
        password_hash="dfkjs984w9f09343", is_blocked=False, prescs = []):
        self.__username = username
        self.__is_logged_in = is_logged_in
        self.__password_hash = password_hash
        self.__is_blocked = is_blocked
        self.__prescs = prescs
        super().__init__()

    def addPrescription(self, presc):
        self.__prescs.append(presc)
    
    def setPrescriptions(self, prescriptions):
        self.__prescs = prescriptions

    def getPrescriptions(self):
        return self.__prescs

    def createOrder(self, pd):
        order = Order()
        order.setPrescDetail(pd)
        return order
    
    def getUsername(self):
        return self.__username
    
    def setUsername(self, username):
        self.__username = username
    
    def __str__(self):
        return f"User: {super().__str__()} username: {self.__username}"
