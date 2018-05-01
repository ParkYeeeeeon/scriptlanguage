def decimalToHex(value):
    if value==0:
        return ""
    else:
        r=value%16
        if r>=10:
            temp=chr(ord('A')+r-10)
        else:
            temp=str(r)
        return decimalToHex(value//16)+temp


value=eval(input("10진수 입력"))
print(value,"를 16진수로 바꾸면",decimalToHex(value))