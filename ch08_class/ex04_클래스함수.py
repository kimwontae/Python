# 인스턴스 메소드:
# - 각 객체에서 개별적으로 동작하는 함수
# - 첫 인자로 self가 필요함

class Car():
    #클래스 변수 
    instance_count = 0

    def __init__(self, size, color):
        self.size = size
        self.color = color
        Car.instance_count= Car.instance_count +1
        print("자동차 객체의 수 : {0}".format(Car.instance_count))

    def move(self, speed):
        self.speed = speed
        print("자동차{0} # {1}가 움직입니다.".format(self.size, self.color), end ='')
        print("시속: {0}".format(self.speed))

    #정적 메소드
    @staticmethod
    def check_type(model_code):
        if(model_code >= 20):
            print("이 자동차는 전기임")
        elif(10 <= model_code<20):
            print("이 자동차는 가솔린임")
        else:
            print("이 자동차는 디젤임")

    #클래스 메소드
    @classmethod
    def count_instance(cls):
        print("자동차 객체의 개수 ".format(cls.instance_count))



car1=Car("small", "red")
car2=Car("big", "green")

car1.move(10)
car2.move(20)



#정적 메소드
# - 클래스나 클래스의 인스턴스 와는 무관하게 독립적으로 동작한다.
# - self를 사용하지 않으며 정적 메소드 안에서는 인스턴스 메소드나 
# 인스턴스 변수에 접근 할 수 없다.

Car.check_type(20)
Car.check_type(10)
Car.check_type(50)


#클래스 메소드
# - 클래스 변수를 사용하기 위한 함수
# - 첫 번째 인자로 클래스를 넘겨받는 cls가 필요
# - @classmethod 를 지정

car1=Car("small", "red")
Car.count_instance()


