r=int(input("연이율입력:"))
a=int(input("매달 저축할 금액:"))

r_month=(r/100)/12
for n in range(1,12):
    a=(1+r_month)*a
    print(a)
