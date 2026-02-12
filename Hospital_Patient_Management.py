class Patient:
    consultation_fee = 500
    room_charge_per_day = 1000
    
    def __init__(self, pname, pid):
        self.pname = pname
        self.pid = pid
        self.admitted = False

    def admit_patient(self, pid, pname, disease):
        if self.admitted == True:
            print(self.pname, ",You are already admitted", sep="")
            return
        self.admitted = True
        print(self.pname, ",Admitted for ", disease, sep="")

    def discharge_patient(self, pid, pname, days):
        if self.admitted == False:
            print(self.pname, ",You are not admitted", sep="")
            return
        print(self.pname, ",Discharged successfully", sep="")
        Patient.calculate_bill(self, days)
        self.admitted = False

    def calculate_bill(self, days):
        if self.admitted == False:
            print("No active admission to calculate bill")
            return
        total = (days * Patient.room_charge_per_day) + Patient.consultation_fee
        print("Total bill is: ", total)

    @classmethod
    def update_consultation_fee(cls, new_fee):
        cls.consultation_fee = new_fee
        print("Consultation fee updated to: ", cls.consultation_fee)


# Objects
p1 = Patient("Sri", 201)
p1.admit_patient(201, "Sri", "Fever")

p2 = Patient("Padma Sri", 202)
p2.admit_patient(202, "Padma Sri", "Infection")

p1.discharge_patient(201, "Sri", 3)
p1.calculate_bill(5)

Patient.update_consultation_fee(700)

p2.discharge_patient(202, "Padma Sri", 2)
