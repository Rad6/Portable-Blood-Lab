from Prescription import Prescription

class User:
    def __init__(self, is_logged_in, password_hash, is_blocked, prescs = []):
        self.__is_logged_in = is_logged_in
        self.__password_hash = password_hash
        self.__is_blocked = is_blocked
        self.__prescs = prescs

    def getPrescriptions(self):
        return self.__prescs

    def createOrder(self, pd):
        # TODO
        pass

    
