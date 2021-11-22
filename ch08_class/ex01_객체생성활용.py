#class선언
class Bicycle():
    #클래스 변수
    def move(self, speed):
        print("자전거 시속 {0}으로 전진".format(speed))
    def turn(self, direction):
        print("자전거 방향 {0}회전".format(direction))
    def stop(self):
        print("자전거 바퀴크기: {0}, 색상: {1}".format(self.wheel_size, self.color))

#객체 생성
#객체명 = 클래스명()
my_bicycle = Bicycle()
print(my_bicycle)
#<__main__.Bicycle object at 0x7fe4181b3dc0>

#객체에 속성 설정
#객체명.변수명 = 속성값
my_bicycle.wheel_size=26
my_bicycle.color = 'black'

print("바퀴크기: ",my_bicycle.wheel_size)
print("색상: ",my_bicycle.color)

#객체의 메소드 호출
my_bicycle.move(30)
my_bicycle.turn('left')
my_bicycle.stop()


#객체 생성
bicycle1 = Bicycle()
bicycle1.wheel_size=27
bicycle1.color='red'

bicycle1.move(20)
bicycle1.turn('right')
bicycle1.stop()


bicycle2=Bicycle()
bicycle2.wheel_size=24
bicycle2.color='blue'

bicycle2.move(40)
bicycle2.turn('left')
bicycle2.stop()