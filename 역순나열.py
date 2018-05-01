st=input("정수 입력")
stList = st.split()
inList=[eval(i) for i in stList]

for i in range(len(inList)-1,-1,-1):
    print(inList[i],end=" ")

inList.reverse()
print("")
