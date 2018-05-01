def decimalToBinary(value):
    if value==0:
        return ""
    else:
        r=value%2
        return decimalToBinary(value//2)+str(r)


value=eval(input("10진수 입력"))
print(value,"를 이진수로 바꾸면",decimalToBinary(value))