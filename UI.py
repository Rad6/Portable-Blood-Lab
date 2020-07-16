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

    def enterPrescriptionID(self):
        print("Enter your Priscription ID: ", end="")
        pid = int(input())
        self.__handler.enterPrescriptionID(pid)
        print("Order with pid=" + str( (self.__handler).getOrder().getPrescDetail().getPrescID() ) + " created\n")

    def chooseTest(self):
        print("Your Priscription includes following tests:")

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


if __name__ == "__main__":
    ui = UI()
    # ui.chooseTime()
    ui.enterPrescriptionID()
    ui.chooseTest()