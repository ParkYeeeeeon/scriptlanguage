def num(i):
    if i==1:
        return 1/2
    else:
        return num(i-1) +i/(i+1)

for i in range(1,21):
    if i==1:
        print("i의 값\tnum(i)")
    print(i,"\t",num(i))