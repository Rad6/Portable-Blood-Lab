from PaymentGateway import PaymentGateway, PaymentStatus

class PaymentDetail:
    def __init__(self, amount=.0, status=PaymentStatus.no_status, \
        tracking_code="no-trackingcode"):
        self.__amount = amount
        self.__status = status
        self.__tracking_code = tracking_code

    def setAmount(self, value):
        self.__amount = value

    def pay(self):
        payment_gateway = PaymentGateway()
        res = payment_gateway.pay(self.__amount)
        self.setStatus(res['status'])
        self.setTrackingCode(res['trackingcode'])
        return res

    def setStatus(self, value):
        self.__status = value

    def setTrackingCode(self, value):
        self.__tracking_code = value
    
    def __str__(self):
        return f"PaymentDetail: amount: {self.__amount}, status: \
            {self.__status}, trackingcode: {self.__tracking_code}"