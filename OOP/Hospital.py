import random

class Patient(object):
    def __init__(self, id_number, name, allergies):
        self.id_number = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = None
    def info(self):
        print "ID: " + str(self.id_number)
        print "Name: " + self.name
        print "Allergies: " + str(self.allergies)
        print "Bed #: " + str(self.bed_number)
        return self
    def addBed(self, number):
        self.bed_number = number

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def admit(self, patient):
        if self.capacity == len(self.patients):
            print "the hospital is full"
            return self
        else:
            self.patients.append(patient)
            bednum = random.randint(0,len(self.patients))
            patient.addBed(bednum)
            return self
    def discharge(self, patient):
        self.capacity-=1
        patient.addBed(None)
        return self
    def info(self):
        print "The current patients:" +  str(self.patients)
        print "Hospital name: " + self.name
        print "Capacity: " + str(self.capacity)
        return self

patient1 =  Patient("001", "Anton Test", None)
patient2 =  Patient("002", "Mark Levy", "Chocolate")
patient3 =  Patient("003", "Aer Muhanfy", "Chocolate, Smoke, Sea-food, Honey")
patient4 =  Patient("004", "John Godiva", "Ampicillin")

patient1.info()

c1 = Hospital("St. Mark",10)

c1.info()

c1.admit(patient1).admit(patient2).info

patient1.info()
patient2.info()

c1.admit(patient3).admit(patient4).discharge(patient1).info

patient1.info()
patient2.info()
patient3.info()
patient4.info()