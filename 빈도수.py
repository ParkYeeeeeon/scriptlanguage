st1 = input("1과 100 사이 정수 입력")
l = st1.split()
intList = [eval(i) for i in l]
frequency = []

for i in range(100):
   frequency.append(0)

for i in intList :
   frequency[i-1] += 1

for i in range(100):
    if frequency[i] > 0:
        print("{0:3} - {1}번 나타남".format(i + 1, frequency[i]))
