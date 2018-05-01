a,b,c=eval(input("a,b,c 입력:"))
print(a,b,c)

determinant=b**2-4*a*c
if determinant>0:
    r1=(-b-determinant**0.5)/2*a
    r2 = (-b + determinant ** 0.5) / 2 * a
    print("실근은 {0:.2f},{1:.2f}입니다".format(r1,r2))
elif determinant==0:
    r1 = (-b - determinant ** 0.5) / 2 * a
    print("실근은",r1,"입니다")
elif determinant<0:
    print("이 방정식은 실근이 존재하지 않습니다")
