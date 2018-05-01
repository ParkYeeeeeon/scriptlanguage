def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)

m,n=eval(input("두 정수형, 구분해서 입력:"))

print(m,"과",n,"의 최대 공약수=",gcd(m,n))