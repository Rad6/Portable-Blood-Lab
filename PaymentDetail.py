
class PaymentDetail:
    def __init__(self, amount, status, tracking_code):
        self.__amount = amount
        self.__status = status
        self.__tracking_code = tracking_code

    def setAmount(self, value):
        self.__amount = value

    def pay(self):
        # TODO
        pass

    def setStatus(self, value):
        self.__status = value

    def setTrackingCode(self, value):
        self.__tracking_code = value
