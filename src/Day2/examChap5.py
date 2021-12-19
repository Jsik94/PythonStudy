# 연습문제
# https://wikidocs.net/42529
import random
import sys
import glob
import os

#Q1
import time


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

#상속에 관한 문제
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -=val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print("1]",cal.value)

# Q2
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value+=val
        self.value = 100 if self.value > 100 else self.value

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print("2]",cal.value) # 100 출력


#Q3
print("3-1] 거짓 -> 0이 존재")
print("3-2] 참 -> 유니코드값을 다시 char형으로 전환")

#Q4
sample = [1, -2, 3, -5, 8, -3];
result = list(filter(lambda x : x > 0 ,sample))
print("4]",result)
print("만약 음수는 양수로 바꾼뒤 +2 해준 값으로 바꾸고 싶다면 ? ")
result2=list(map(lambda x: abs(x)+2 if x <0 else x, sample))
print("4-1]",result2)


#Q5
print("5]",int(0xea))


#Q6
print("6]",list(map(lambda x: x*3, [1, 2, 3, 4])))

#Q7
print("7]","최대",max([-8, 2, 7, 5, -3, 5, 0, 1]),"최소",min([-8, 2, 7, 5, -3, 5, 0, 1]))

#Q8
print("8]",round(17/3*10000)/10000)
print("8]",round(17/3,4))


#Q9

#내일 다시봐야함
import sys

numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)
print("9]",result)


#Q10
#popen os명령어 실행시 결과값을 저장 read 으로 출력가능
result = os.popen("dir")
print("10]",result.read())

#Q11

print("11]",glob.glob("C:\\Users\\yoonsic\\IdeaProjects\\PythonStudy\\src\\Day2\\*.py"))


#Q12
#2018/04/03 17:20:32
# time.strftime -> simple date Format
# time.localtime -> Date랑 같은 느낌
# time.time() -> getTime 과 같음
print("12]",time.strftime('%Y/%m/%d %X',time.localtime(time.time())))


#Q13

result = []
print("13]",end='')

while True:
    num = random.randrange(1,45)
    if num is not result :
        result.append(num)

    if len(result) is 6 :
        break;
print(result)