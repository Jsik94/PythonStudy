#   Link
#   https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    curL=10
    curR=12
    for num in numbers:
        if num in [1,4,7] :
            answer +='L'
            curL =num
        elif num in [3,6,9] :
            answer +='R'
            curR =num
        else :
            num = num if num != 0 else 11
            Ldist = getCount(curL,num)
            Rdist = getCount(curR,num)
            if Ldist == Rdist :
                if hand == "left":
                    answer+= "L"
                    curL=num
                else:
                    answer+= "R"
                    curR=num
            else :
                if Ldist < Rdist:
                    answer+= "L"
                    curL=num
                else :
                    answer+="R"
                    curR=num

    return answer

def getCount(loc,num):
    cnt =0
    #첫번째 라인
    if loc %3 ==1 :
        cnt+=1
        loc+=1
    #세번째 라인
    elif loc % 3 ==0:
        cnt+=1
        loc-=1
    cnt += int(abs(num-loc)/3)
    return cnt