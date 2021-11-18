#단일 조건에 따른 분기
x=95
if x>= 90:
    print("축하합니다")
    print("당신은 합격입니다.")

#단일 조건 및 그 외 조건에 따른 분기(if~else)
x=75
if x>=90:
    print("pass")
else:
    print("fail")


#여러 조건에 따른 분기 (if~elif~else)

x=85
if x>=90:
    print("verygood")
elif (x>=80)and (x<90):
    print("good")
else:
    print("bad")



#중첩 조건에 따른 분기
x=190
if x>=90:
    if x==100:
        print("prtfect")
    else:
        print("very good")
elif (x>=80) and (x<90):
    print("good")
else:
    print("bad")