


def generateSampleTestsAllType():
    from Test import Test
    tests = [
        Test('Thyroid', mustinclucepresc=True),
        Test('HIV', mustinclucepresc=True),
        Test('Herpes', mustinclucepresc=True),
        Test('Vitamin D', mustinclucepresc=False),
        Test('Sodium', mustinclucepresc=False),
        Test('Calcium', mustinclucepresc=False)
    ]
    return tests

def generateSampleBloodExperts():
    from BloodExpert import BloodExpert
    from Location import Location
    from DailySchedule import DailySchedule
    from Date import Date
    from ServiceTime import ServiceTime, DateType
    blood_experts = [
        BloodExpert(1, Location(10, 10), [
            DailySchedule(Date(2020, 9, 5, 0), [
                ServiceTime(Date(2020, 7, 2, 16)), # OLD DATE
                ServiceTime(Date(2020, 9, 5, 8)),
                ServiceTime(Date(2020, 9, 5, 10)),
                ServiceTime(Date(2020, 9, 5, 12), True, DateType.special),
                ServiceTime(Date(2020, 9, 5, 14)),
            ]),
            DailySchedule(Date(2020, 9, 6, 0), [
                ServiceTime(Date(2020, 9, 6, 8)),
                ServiceTime(Date(2020, 9, 6, 10)),
                ServiceTime(Date(2020, 9, 6, 16)),
                ServiceTime(Date(2020, 9, 6, 14)),
            ])
        ]),
        BloodExpert(2, Location(30, 25), [
            DailySchedule(Date(2020, 9, 7, 0), [
                ServiceTime(Date(2020, 9, 7, 8)),
                ServiceTime(Date(2020, 9, 7, 10)),
                ServiceTime(Date(2020, 9, 7, 12), True, DateType.special),
                ServiceTime(Date(2020, 9, 7, 14)),
            ]),
            DailySchedule(Date(2020, 9, 8, 0), [
                ServiceTime(Date(2020, 9, 8, 8)),
                ServiceTime(Date(2020, 9, 8, 10)),
                ServiceTime(Date(2020, 9, 8, 16), False),
                ServiceTime(Date(2020, 9, 8, 14)),
            ])
        ]),
    ]
    return blood_experts

def generateSampleLab():
    from Lab import Lab
    lab = Lab('sampleLab1')
    lab.setBloodExperts(generateSampleBloodExperts())
    lab.setTests(generateSampleTestsAllType())
    return lab

def kgenerateTestList():
    from TestList import TestList
    testlist = TestList()
    testlist.setTests(generateSampleTestsAllType())
    return testlist

def kgeneratePrescriptionDetail():
    from PrescriptionDetail import PrescriptionDetail
    pd = PrescriptionDetail()
    pd.setIsAccepted(True)
    pd.setIsCovered(True)
    pd.setTests(kgenerateTestList())
    return pd

def generateSampleOrder():
    from Order import Order
    order = Order()
    order.setLab(generateSampleLab())
    order.setTestList(kgenerateTestList())
    order.setPrescDetail(kgeneratePrescriptionDetail())
    return order

def generateSamplePrescDetail(presc_id, covered):
    from PrescriptionDetail import PrescriptionDetail
    _tests = generateSampleTestsAllType()
    presc_detail = PrescriptionDetail(prescID=presc_id, isCovered=covered, isAccepted=True, tests= _tests)
    return presc_detail

def generateSampleCheckedPresc(presc_id, covered):
    from Prescription import Prescription
    presc = Prescription()
    presc_detail = generateSamplePrescDetail(presc_id, covered)
    presc.setPrescriptionDetail(presc_detail)
    return presc

def generateSampleUserWithPrescs():
    from User import User
    prescriptions = []
    n_prescs = 10
    for i in range(n_prescs):
        presc = generateSampleCheckedPresc(i, True)
        prescriptions.append(presc)
    user = User(username='sampleUserName', is_logged_in=True)
    user.setPrescriptions(prescriptions)
    return user

def hGenerateSampleUserWithoutPrescs():
    from User import User
    user = User(username='sampleUserName', is_logged_in=True)
    return user

def hGenerateSampleLabsWithTests():
    from Lab import Lab
    from Test import Test
    labs = []

    lab1 = Lab('sampleLab1')
    lab1.setBloodExperts(generateSampleBloodExperts())
    tests = [
        Test('Thyroid', mustinclucepresc=True),
        Test('HIV', mustinclucepresc=True),
        Test('Herpes', mustinclucepresc=True),
        Test('Vitamin D', mustinclucepresc=False),
        Test('Sodium', mustinclucepresc=False),
        Test('Calcium', mustinclucepresc=False)
    ]
    lab1.setTests(tests)
    labs.append(lab1)

    lab2 = Lab('sampleLab2')
    lab2.setBloodExperts(generateSampleBloodExperts())
    tests = [
        Test('HIV', mustinclucepresc=True),
        Test('Herpes', mustinclucepresc=True),
        Test('Vitamin D', mustinclucepresc=False),
        Test('Sodium', mustinclucepresc=False),
        Test('Calcium', mustinclucepresc=False),
        Test('Corona', mustinclucepresc=False)
    ]
    lab2.setTests(tests)
    labs.append(lab2)

    lab3 = Lab('sampleLab3')
    lab3.setBloodExperts(generateSampleBloodExperts())
    tests = [
        Test('Herpes', mustinclucepresc=True),
        Test('Vitamin D', mustinclucepresc=False),
        Test('Sodium', mustinclucepresc=False),
        Test('Calcium', mustinclucepresc=False),
        Test('Corona', mustinclucepresc=False),
        Test('FBG', mustinclucepresc=False)
    ]
    lab3.setTests(tests)
    labs.append(lab3)

    lab4 = Lab('sampleLab4')
    lab4.setBloodExperts(generateSampleBloodExperts())
    tests = [
        Test('Thyroid', mustinclucepresc=True),
        Test('HIV', mustinclucepresc=True),
        Test('Herpes', mustinclucepresc=True),
        Test('Vitamin D', mustinclucepresc=False),
        Test('Sodium', mustinclucepresc=False),
        Test('Calcium', mustinclucepresc=False),
        Test('Corona', mustinclucepresc=False),
        Test('FBG', mustinclucepresc=False)
    ]
    lab4.setTests(tests)
    labs.append(lab4)

    return labs

def hGenerateAllOTCTests():
    from Test import Test
    tests = [
        Test('Vitamin D', mustinclucepresc=False),
        Test('Sodium', mustinclucepresc=False),
        Test('Calcium', mustinclucepresc=False),
        Test('Corona', mustinclucepresc=False),
        Test('FBG', mustinclucepresc=False)
    ]
    return tests