
class PaymentGateway:
    def __init__(self, endpoint, api_key):
        self.__endpoint = endpoint
        self.__api_key = api_key

    def pay(self, amount):
        # TODO
        pass

    def getAPIKey(self):
        return self.__api_key

    def getEndPoint(self):
        return self.__endpoint
    
