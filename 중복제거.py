str=input("10개의 숫자를 입력:")
stringList=str.split()
list1=[]
list2=[]
for s in stringList:
    list1.append(eval(s))
for n in list1:
    if not n in list2:
        list2.append(n)
print("중복을 제거한 고유한 숫자:",list2)