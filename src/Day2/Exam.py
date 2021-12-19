# 디렉토리는 그냥 import
import test
# from으로 경로를 지정하고 그 내부에 있는 파일을 불러올 수 있음
# as는 alias
from test import dirTest as tt


print("실행하는 Main 문!")


print("<-- test Dir에 있는 변수 호출하기 -->")
print(test.a)
print(test.b)


print("<-- test Dir에 있는 변수 호출하기 -->")
print(tt.a)
print(tt.b)


class Sample:
    def something(self,first,*second):
        print("aa")
        return


test = Sample()
test.something(1)
test.something(1,2)