class Person:
    def __init__(self,name,number):
        self.name = name
        self.number=number
    def __str__(self):
        return "이름 = "+self.name+"\n주민번호 = "+self.number
class Student(Person):
    def __init__(self,name,number,classes,gpa):
        super().__init__(name,number)
        self.classes=classes
        self.gpa=gpa
    def __str__(self):
        return super().__str__()+"\n수강과목 = "+str(self.classes)+"\ngpa = "+str(self.gpa)
class Teacher(Person):
    def __init__(self,name,number,courses,salary):
        super().__init__(name,number)
        self.courses=courses
        self.salary=salary
    def __str__(self):
        return super().__str__()+"\n강의과목 = "+str(self.courses)+"\n월급 = "+str(self.salary)

s = Student("박연","12345",['파이썬','특강'],4.5)
t = Teacher("김철수",'1234567890',['파이썬'],3000000)
print(s)
print(t)