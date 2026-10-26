class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, amount):
        self.__bill_amount = amount

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount, discount, final_bill):
        self.__name = name
        self.__bill_amount = bill_amount
        self.__discount = discount
        self.__final_bill = final_bill

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def get_discount(self):
        return self.__discount

    def get_final_bill(self, bill_amount, discount):
        self.__final_bill = bill_amount - (bill_amount * discount)
        return self.__final_bill

class PhilHealthPatient:
    def __init__(self, name, bill_amount, discount, final_bill):
        self.__name = name
        self.__bill_amount = bill_amount
        self.__discount = discount
        self.__final_bill = final_bill

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def get_discount(self):
        return self.__discount

    def get_final_bill(self, bill_amount, discount):
        self.__final_bill = bill_amount - (bill_amount * discount)
        return self.__final_bill


patient2 = SeniorPatient("Rasulity", 15000, 0.2, 0)
patient1 = Patient("Maurisity", 15000)
patient3 = PhilHealthPatient("Alwinity", 15000, 0.15, 0)

print("\n Hospital Billing System ")
print("---------------------------")
print("Patient Name:", patient1.get_name())
print("Original Bill:", patient1.get_bill_amount())
print("Final Bill:", patient1.get_bill_amount())

print("\n Hospital Billing System ")
print("---------------------------")
print("Patient Name:", patient2.get_name())
print("Original Bill:", patient2.get_bill_amount())
print("Final Bill:", patient2.get_final_bill(patient2.get_bill_amount(), patient2.get_discount()))

print("\n Hospital Billing System ")
print("---------------------------")
print("Patient Name:", patient3.get_name())
print("Original Bill:", patient3.get_bill_amount())
print("Final Bill:", patient3.get_final_bill(patient3.get_bill_amount(), patient3.get_discount()))



