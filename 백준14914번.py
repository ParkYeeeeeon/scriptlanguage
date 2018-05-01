def dividefruits(a,b):
    i=[]
    if (a>=b):
        for n in range(1,a+1):
            if (a%n==0)and(b%n==0):
                i.append(n)
                print(n,a/n,b/n)
    else:
        for n in range(1,b+1):
            if (a % n == 0) and (b % n == 0):
                i.append(n)
                print(n, a / n, b / n)


a,b=(eval(input())).split(' ')
dividefruits(a,b)
