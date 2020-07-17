from Handler import Handler
from enum import Enum


class OrderType(Enum):
    with_presc = 1
    without_presc = 2
    with_fault_code = 3
    

class UI:

    def __init__(self):
        self.__handler = Handler()
        self.__has_presc = None
        self.__order_type = None

    def chooseTime(self):
        with_fault_code = False
        if self.__order_type == OrderType.with_fault_code:
            with_fault_code = True
        total_times = self.__handler.getTimes(with_faultcode = with_fault_code)
        
        print("\t0 : back")
        for i, item in enumerate(total_times):
            print(f"\t{i+1} : {item}")
        
        print("Choose a time from times above: ", end="")
        while True:
            try:
                chosen_time = int(input())
            except ValueError:
                print("Invalid, Try Again; ", end="")
                continue                
            if chosen_time >= 0 and chosen_time <= len(total_times):
                break
            else:
                print("Invalid, Try Again, ", end="")
        
        if chosen_time == 0:
            # TODO: BACK TO PREV SEC
            pass
        else:
            self.__handler.chooseTime(total_times[chosen_time-1])
            print(f"the time is successfully added")
            # TODO: back to the menu

    def getPrice(self):
        totalprice = self.__handler.getPrice()
        print(f"the total price is : {totalprice}")
        # TODO: Show menu based on the price {cancel or stuff or back}

    def enterPrescriptionID(self):
        print("Enter your Priscription ID: (between 0 and 9, fake!) ", end="")
        while True:
            pid = int(input())
            try:
                self.__handler.enterPrescriptionID(pid)
            except:
                print("not found, try again: ", end="")
                continue
            # self.__handler.enterPrescriptionID(pid)
            print("Order with pid=" + str( (self.__handler).getOrder().getPrescDetail().getPrescID() ) + " created\n")
            break

    def chooseTest(self):
        if self.__order_type == OrderType.with_presc:
            print("Your Priscription includes following tests:")
        else:
            print("Available OTC tests are:")


        tests = self.__handler.getTests()
        for i in range(len(tests)):
            print(str(i) + ". " + tests[i].getName())
        
        print("Enter the tests numbers from above to finilize your order(in one line, space separated) :")
        while True:
            valid = True
            try:
                final_tests_numbers = list(map(int, input().split()))
                for each in final_tests_numbers:
                    if each >= len(tests):
                        valid = False
                        print("Invalid, please try again: ", end="")
                        break
            except:
                valid = False
                print("Invalid, please try again: ", end="")
                continue
            if valid:
                break

        final_tests = []
        for each in final_tests_numbers:
            final_tests.append(tests[each])

        self.__handler.chooseTests(final_tests)

        print("You've chosen: ")
        for each in self.__handler.getOrder().getTestList().getTests():
            print(each.getName(), end=" ")
        print("\n")

    def chooseLab(self):
        final_labs = self.__handler.getLabs()
        print("Labs that support your tests are:")
        for i in range(len(final_labs)):
            print(str(i) + ". " + final_labs[i].getName())

        if final_labs[0].getName() == "sampleLab1":
            print("Choose your lab: (enter number. Orders on our lab (sampleLab1), will get a 5% discount)")
        else:
            print("Choose your lab: (enter number)")


        while True:
            valid = True
            try:
                chosen_lab_num = int(input())
                if chosen_lab_num >= len(final_labs):
                    valid = False
                    print("Invalid, please try again: ", end="")
                    continue
            except ValueError:
                valid = False
                print("Invalid, please try again: ", end="")
                continue
            if valid:
                break

        self.__handler.chooseLab(final_labs[chosen_lab_num])
        print("You've chosen " + self.__handler.getOrder().getLab().getName() + " lab.")


    def payOnline(self):
        res = self.__handler.payOnline()
        print(f"Payment Status is : {res['status']}, TrackingCode: {res['trackingcode']}")

    def assignExpert(self):
        self.__handler.getOrder().getLab().assignExpert(self.__handler.getOrder())
        print("Expert with id:" +str( self.__handler.getOrder().getBloodExpert().getID() )+ " assigned.")

    def enterAddress(self):
        print("enter your addres: ", end="")
        address = str(input())
        self.__handler.enterAddress(address)
        print("done!")

    def createOrder(self):
        print("Do you have a PrescriptionId? (y/n)")
        ans = input()
        if ans == 'y':
            self.__has_presc = True
            self.enterPrescriptionID()
        else:
            self.__has_presc = False
            self.startNewOrder()

    def startNewOrder(self):
        self.__handler.startNewOrder()
        print("New order created!\n")
    
    def enterFaultCode(self):
        print("enter your faultcode: ", end="")
        while True:
            faultcode = str(input())
            
            status = self.__handler.enterFaultCode(faultcode)
            if status:
                print("done!")
                break
            else:
                print("there is no such faultcode, try again: ", end="")

    def ask_order_type(self):
        print("Please choose one of the following:\n" +
        "1. New order with prescription\n" + 
        "2. New order without prescription\n" +
        "3. Enter fault code"
        )
        while True:
            try:
                order_type = int(input())
            except ValueError:
                print("Invalid. Try again: ", end="")
                continue
            if order_type == 1:
                self.__order_type = OrderType.with_presc
            elif order_type == 2:
                self.__order_type = OrderType.without_presc
            elif order_type == 3:
                self.__order_type = OrderType.with_fault_code
            else:
                print("Invalid. Try again: ", end="")
                continue
            break

    def getOrderType(self):
        return self.__order_type
    

if __name__ == "__main__":
    ui = UI()
    ui.ask_order_type()
    if ui.getOrderType() == OrderType.with_presc:
        ui.enterPrescriptionID()
    elif ui.getOrderType() == OrderType.without_presc:
        ui.startNewOrder()
    else:
        ui.enterFaultCode()

    if ui.getOrderType() != OrderType.with_fault_code:
        ui.chooseTest()
        ui.chooseLab()

    ui.chooseTime()

    if ui.getOrderType() != OrderType.with_fault_code:
        ui.enterAddress()
        ui.assignExpert()
        ui.getPrice()
        ui.payOnline()
