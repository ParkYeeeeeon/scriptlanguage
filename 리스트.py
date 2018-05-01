def isAnagram(s1,s2):

    list1 = []
    list2 = []
    for s in s1:
        list1.append(s)
    for n in s2:
        list2.append(n)

    list1.sort()
    list2.sort()
    if(list1==list2):
        return True


s1=input("첫째")
s2=input("둘째")
if isAnagram(s1,s2):
    print("애너그램")
else:
    print("아님")