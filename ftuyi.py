class Vehicle:
    def __init__(self, name):
        self.name = name

class Car:
    def introduce_doctor(self, doctor):
        print(f"Мой врач: {doctor.name}")
doctor = Doctor("Иванов Иван")
patient = Patient('Петроп')
patient.introduce_doctor(doctor)