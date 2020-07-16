from enum import Enum


class PaymentStatus(Enum):
    ok = 1
    faild = 2
    no_status = 3
    
class PaymentGateway:
    def __init__(self, endpoint="https://bank.com/pay", api_key="j9rsdf8j39jg"):
        self.__endpoint = endpoint
        self.__api_key = api_key

    def pay(self, amount):
        api_key = self.getAPIKey()
        endpoint = self.getEndPoint()
        # :) there is no Payment Provider so, we return the artificial status
        return {
            'status' : PaymentStatus.ok,
            'trackingcode' : "23850981239"
        }

    def getAPIKey(self):
        return self.__api_key

    def getEndPoint(self):
        return self.__endpoint
    
