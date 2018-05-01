name = input("사원 이름을 입력하세요 : ")
weekstime = eval(input("주 당 근무시간을 입력하세요 : "))
pay = eval(input("시간 당 급여를 입력하세요 : "))
tax = eval(input("원천징수세율을 입력하세요 : "))
localtax = eval(input("지방세율을 입력하세요 : "))

money = weekstime * pay
taxed = int(money * tax)
localtaxed = int(money * localtax)
taxsum = taxed + localtaxed

realmoney = money - taxsum

print("사원 이름 : ",name,"\n주 당 근무시간 : ",weekstime,"\n임금 : ",pay,
      "\n총 급여 : ",money,"\n공제 : \n  원천징수세(",tax * 100,"%) : ",taxed,
      "\n  주민세(",localtax * 100,"%) : ",localtaxed,"\n  총 공제 : ",taxsum,
      "\n 공제 후 급여 : ",realmoney)
