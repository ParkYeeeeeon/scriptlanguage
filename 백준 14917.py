from datetime import datetime


def jesonghabnida():
    if datetime.today().month!=11:
        if datetime.today().day!=11:
            print("오늘은")
            print("빼배로데이가 아닙니다....너무 어려워요 교수님")
            print("죄송합니다....")

print(datetime.today().year)
print(datetime.today().month)
print(datetime.today().day)
jesonghabnida()