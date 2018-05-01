def displaySortedNumber(num1,num2,num3):
    l=[num1,num2,num3]
    l.sort()
    return print(l)

n1,n2,n3=input("숫자 3개 입력:").split(',')
displaySortedNumber(n1,n2,n3)