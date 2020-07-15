


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

def generateSampleOrder():
    from Order import Order
    order = Order()
    order.setLab(generateSampleLab())
    return order