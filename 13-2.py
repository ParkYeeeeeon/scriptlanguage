filename=input("파일 이름 입력: ")

inputfile=open(filename,"r")
inputStr=inputfile.read()

print("문자{0}개".format(len(inputStr)))
print("단어{0}개".format(len(inputStr.split())))
print("행{0}개".format(len(inputStr.split("\n"))))

