class Car():
    #클래스 변수
    instance_count = 0;

    #초기화 함수
    def __init__(self, size, color):
        self.size = size
        self.color = color
        Car.instance_count=Car.instance_count +1
        print("자동차 객체의 수 : {0}".format(Car.instance_count))
    
    #클래스 함수
    def move(self):
        print("자동차{0} $ {1}로 움직인다".format(self.size, self.color))


#객체 생성
car1=Car('small', 'blue')
car2=Car('big', 'white')

print("car클래스의 인스턴스 총 개수: {}".format(Car.instance_count))

print("car1클래스의 인스턴스 총 개수: {}".format(car1.instance_count))
print("car2클래스의 인스턴스 총 개수: {}".format(car2.instance_count))

car1.move()
car2.move()

class Car2():
    #클래스 변수
    count =0

    #초기화 함수
    def __init__(self, size, num):
        #인스턴스 변수
        self.size = size
        self.num= num
        Car2.count=car2.color +1
        print("자동차 객체의 수 : Car2.count = {0}".format(car2.instance_count))
        print("인스턴스 변수의 수 : self.count = {0}".format(self.count))

        def move(self):
            print("자동차{0} $ {1}가 움직인다".format(self.size, self.count))

car1 = Car2("big", 20)
car2 = Car2("small", 10)


