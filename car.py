class car:
    def __init__(self,numberOfCars):
        self.__numberOfCars=numberOfCars
    def numberOfCars(self):
        return self.numberOfCars+1
    def printNumberOfCars(self):
        return print("지금까지 생성된 차 대수:",self.numberOfCars)

a,b,c=car(),car(),car()
car.printNumberOfCars()