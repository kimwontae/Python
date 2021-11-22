#모듈을 불러오는 다른 형식
#import 모듈
#from 모듈 import 변수명
#from 모듈 import 함수명
#from 모듈 import 클래스명

from my_area import PI
from my_area import square_area
from my_area import circle_area
from my_area import *  #별로 좋지는 않음


print(PI)
print(square_area(2))
print(circle_area(2))