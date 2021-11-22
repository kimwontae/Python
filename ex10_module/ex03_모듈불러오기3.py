from my_module2 import *
from my_module1 import *


func1()
func2()
func3()


#모듈명을 별명으로 선언

import my_area as area

print('pi=', area.PI)
print('sq=',area.square_area)
print('c=',area.circle_area)

from my_area import PI as pi
from my_area import square_area as sq
from my_area import circle_area as c

print('pi=', pi)
print('sq=',sq)
print('c=',c)
