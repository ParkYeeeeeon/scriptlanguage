class Person:   #부모 클래스
    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber
    def PrintInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))
    def PrintPersonData(self):
        print("Person(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

class Strudent(Person):
    def __init__(self,name,phoneNumber,subject,studentID):
        self.Name = name
        self.PhoneNumber = phoneNumber
        self.Subject = subject
        self.StudentID = studentID