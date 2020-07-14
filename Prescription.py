from PrescriptionDetail import PrescriptionDetail

class Prescription:
    def __init__(self):
        self.__prescriptionDetail = None
        self.__picture = None
        self.__uploadingDate = None
        self.__checkingDate = None
        self.__isChecked = False

    def getPrescriptionDetail(self):
        return self.__prescriptionDetail

    def setPrescriptionDetail(self, prescriptionDetail):
        self.__prescriptionDetail = prescriptionDetail

    def getPicture(self):
        return self.__picture

    def setPicture(self, picture):
        self.__picture = picture

    def getUploadingDate(self):
        return self.__uploadingDate

    def setUploadingDate(self, uploadingDate):
        self.__uploadingDate = uploadingDate

    def getCheckingDate(self):
        return self.__checkingDate

    def setCheckingDate(self, checkingDate):
        self.__checkingDate = checkingDate

    def getIsChecked(self):
        return self.__isChecked

    def setIsChecked(self, isChecked):
        self.__isChecked = isChecked