def reverse(number):
    result = 0
    while number > 0:
        result = result*10+(number % 10)
        number //= 10
        #print(result,number)
    return result

def isPalindrome(number):
    if number == reverse(number):
        print("True")
    else:
        print("False")

print(reverse(1234),isPalindrome(1234))
print(reverse(1221),isPalindrome(1221))