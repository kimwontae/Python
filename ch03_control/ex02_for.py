#반복문의 필요성
a=0
print(a)

a=a+1
print(a)

a=a+1
print(a)


#for  문의 구조
#for <반복변수> in <반복범위>
#   <코드>
#반복범위 지정
#리스트 이용

for a in [0,1,2,3,4,5]:
    print(a)

myFriends = ['james', 'robert', 'lisa', 'mary']
for myFriends in myFriends:
    print(myFriends)
    '''
    james
    robert
    lisa
    mary
    '''

#range() 함수 이용
#형식: range(start, stop, step)

print(range(0,10,1))
print(list(range(0,10,1)))


for a in range(0,10,1):
    print(a)


print(list(range(0,10,1)))
print(list(range(0,20,5)))
print(list(range(-10,0,1)))

x_list=['x1', 'x2']
y_list=['y1', 'y2']

print("x y")
for x in x_list:
    for y in y_list:
        print(x,y)


names =['james', 'robert', 'lisa', 'mary']
scores=[95,96,97,94]
for k in range(len(names)):
    print(names[k], scores[k])
print()


for name, score in zip(names, scores):
    print(name, score)
        