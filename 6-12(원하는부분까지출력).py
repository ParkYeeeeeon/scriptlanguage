def PrintChars(c1,c2,numberPerLine):
    for x in range(c2-c1):
        print(chr(x+49),end=' ')
        if(x+1)%numberPerLine==0:
            print()


PrintChars(1,ord('K'),10)