filename=input("파일 이름 입력: ")
removeStr=input("제거할 문자열을 입력: ")

inputfile=open(filename,"r")
inputStr=inputfile.read()

outputStr=inputStr.replace(removeStr,"")
inputfile.close()
outputfile=open("test2.txt","w")
print(outputStr,file=outputfile)
outputfile.close()
