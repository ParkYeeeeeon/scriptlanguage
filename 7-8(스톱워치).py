import time

class StopWatch:
    def __init__(self):
        self.__startTime=time.time()

    def getStartTime(self):return self.__startTime
    def getEndTime(self):return self.__endTime

    def start(self):
        self.__startTime=time.time()

    def stop(self):
        self.__endTime=time.time()

    def getElapsedTime(self):
        return (self.__endTime - self.__startTime)*1000

    def test(self,n):
        sum=0
        self.start()
        for i in range(1,n+1):
            sum+=i
            print(sum)
        self.stop()
        print (self.getElapsedTime())


StopWatch.test(1,100000)