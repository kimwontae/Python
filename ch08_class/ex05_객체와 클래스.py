robot_name='R1'
robot_pos=0

def robot_move():
    global robot_pos
    robot_pos=robot_pos+1
    print("{0} postion:{1}".format(robot_name, robot_pos))

robot_move()
# R1 postion: 1

robot1_name ="R1"
robot1_pos=10

def robot1_move():
    global robot1_pos
    robot1_pos=robot1_pos+1
    print("{0} postion:{1}".format(robot1_name, robot1_pos))




robot2_name ="R2"
robot2_pos=100

def robot2_move():
    global robot2_pos
    robot2_pos=robot2_pos+1
    print("{0} postion:{1}".format(robot2_name, robot2_pos))

robot1_move()
robot2_move()







class Robot():
    #초기화 함수 (인스턴스 메소드)
    def __init__(self, name, pos):
        #인스턴스 변수
        self.name=name
        self.pos=pos

    def move(self):
        self.pos=self.pos +1
        print("{0} position :{1}".format(self.name, self.pos))


robot1= Robot("R1", 1)
robot2= Robot("R2", 10)
robot3= Robot("L1", 2)
robot4= Robot("L2", 20)

robot1.move()
robot2.move()
robot3.move()
robot4.move()