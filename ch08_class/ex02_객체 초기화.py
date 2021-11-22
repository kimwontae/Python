class Bicycle():
    #생성자를 호출할때 자동으로 실행하는 함수
    def __init__(self, wheel_size, color):
        self.wheel_size=wheel_size
        self.color=color

    #클래스 함수
    def move(self, speed):
        print("자전거 시속 {0}으로 전진".format(speed))
    def turn(self, direction):
        print("자전거 방향 {0}회전".format(direction))
    def stop(self):
        print("자전거 바퀴크기: {0}, 색상: {1}".format(self.wheel_size, self.color))

my_bicycle = Bicycle(26, 'black')
my_bicycle.move(30)
my_bicycle.turn('좌')
my_bicycle.stop()