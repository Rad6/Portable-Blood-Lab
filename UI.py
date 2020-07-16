from Handler import Handler


class UI:

    def __init__(self):
        self.__handler = Handler()

    def chooseTime(self):
        total_times = self.__handler.getTimes()
        
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
        print("Enter your Priscription ID: ", end="")
        pid = int(input())
        self.__handler.enterPrescriptionID(pid)
        print("Order with pid=" + str( (self.__handler).getOrder().getPrescDetail().getPrescID() ) + " created\n")


if __name__ == "__main__":
    ui = UI()
    # ui.chooseTime()
    ui.getPrice()
    ui.enterPrescriptionID()
