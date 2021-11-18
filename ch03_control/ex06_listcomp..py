#리스트 내포 (list comprehension) : 리스트, 세트, 딕셔너리 내에서 
#실행할 수 있는 한줄 for문
#형식 [<반복실행문> for <반복변수> in <반복범위>]

numbers =[1,2,3,4,5]
square = []
for i in numbers:
    square.append(i**2)

print(square)



#리스트 내포방식
square=[i**2 for i in numbers]
print(square)



#조건문을 포함한 리스트 내포
#[<반복 실행문> for <반복변수> in <반복범위> if <조건문>]

numbers =[1,2,3,4,5]
square = []
for i in numbers:
    if i>=3:
        square.append(i**2)
print(square)

numbers =[1,2,3,4,5]
square = [i**2 for i in numbers if i>=3]
print(square)

