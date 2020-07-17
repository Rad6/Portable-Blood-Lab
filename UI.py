from Handler import Handler


class UI:

    def __init__(self):
        self.__handler = Handler()
        self.__has_presc = None

    def chooseTime(self):
        total_times = self.__handler.getTimes(with_faultcode=False)
        
        print("\t0 : back")
        for i, item in enumerate(total_times):
            print(f"\t{i+1} : {item}")
        

        while True:
            print("Choose a time from times above: ", end="")
            chosen_time = int(input())
            if chosen_time >= 0 and chosen_time <= len(total_times):
                break
            else:
                print("Try Again, ", end="")
        
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
        print("Enter your Priscription ID: (between 1 and 10, fake!) ", end="")
        pid = int(input())
        self.__handler.enterPrescriptionID(pid)
        print("Order with pid=" + str( (self.__handler).getOrder().getPrescDetail().getPrescID() ) + " created\n")

    def chooseTest(self):
        if self.__has_presc:
            print("Your Priscription includes following tests:")
        else:
            print("Available OTC tests are:")


        tests = self.__handler.getTests()
        for i in range(len(tests)):
            print(str(i) + ". " + tests[i].getName())
        
        print("Enter the tests numbers from above to finilize your order(in one line, space separated) :")
        final_tests_numbers = list(map(int, input().split()))

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

        print("Choose your lab: (enter number)")
        chosen_lab_num = int(input())

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
        faultcode = str(input())
        
        status = self.__handler.enterFaultCode(faultcode)
        if status:
            print("done!")
        else:
            print("there is no such faultcode")
    

if __name__ == "__main__":
    ui = UI()
    ui.createOrder()
    ui.chooseTest()
    ui.chooseLab()
    ui.chooseTime()
    ui.enterAddress()
    ui.assignExpert()
    ui.getPrice()
    ui.payOnline()
    # ui.enterFaultCode()