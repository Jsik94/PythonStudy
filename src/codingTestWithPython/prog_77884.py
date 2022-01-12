import math
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        # print('숫자 :' ,i,end=' ')
        answer+=i if isEven(i) else i*(-1)
    return answer


def isEven(num):
    cnt =0
    for k in range(1,int(math.sqrt(num)+1)):
        if num % k ==0:
            cnt+=1 if k*k ==num else 2

            # print('갯수:', cnt)
    return True if cnt%2 ==0 else False