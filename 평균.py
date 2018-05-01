st2 = input("정수 입력")
st2List = st2.split()
inList2 = [eval(i) for i in st2List]

sum(inList2)
average = sum(inList2) / len(inList2)

aboveAverageL = list(filter(lambda i:i >= average, inList2))
belowAverageL = list(filter(lambda i:i < average, inList2))

print("평균보다 높은 점수의 개수 = {0}".format(len(aboveAverageL)))
print("평균보다 낮은 점수의 개수 = {0}".format(len(belowAverageL)))
