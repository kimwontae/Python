#상속에 대하여 이해가 필요하다면 볼것! 간단하지만 명확하게 설명

#클래스 상속
#형식: class 자식 클래스명(부모클래스명):
#   <코드블럭>

class Bicycle():
    def __init__(self, wheel_size, color):
        self.wheel_size=wheel_size
        self.color = color

    def move(self, speed):
        print("{0}의 속도로 달린다!!!".format(speed))

    def turn(self, direction):
        print("{0}방향으로 회전!".format(direction))

    def stop(self):
        print("{0}, {1} 멈춰!".format(self.wheel_size, self.color))


#자식 클래스
class FoldingBicycle(Bicycle):
    def __init__(self, wheel_size, color, state):
        #Bicycle.__init__(self, wheel_size, color)
        super().__init__(wheel_size,color)
        self.state=state

    def fold(self):
        self.state='fording'
        print("자전거 접는다! state={0}".format(self.state))

    def unfold(self):
        self.state='unfold'
        print("자전거 안접는다! state={0}".format(self.state))


#객체 생성
foldingBicycle=FoldingBicycle(27, 'white', 'unfolding')
foldingBicycle.move(10)
foldingBicycle.fold()
foldingBicycle.unfold()
