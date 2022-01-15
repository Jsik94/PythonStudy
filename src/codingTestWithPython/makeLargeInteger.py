import itertools

def solution(number, k):
    answer = ''
    data= list(number)
    pers = "0"
    for atom in itertools.combinations(list(number),len(number)-k):
        num = "".join(atom)
        if num > pers:
            pers = num
    return pers

import itertools

def solution2(number, k):
    answer = []
    ans_size = 0
    num = list(map(int,number))
    while ans_size < len(number)-k:
        data = num.copy()
        # print('찾아야 하는 숫자 수', len(number)-k-len(answer))
        while True:
            target = max(data)
            idx = data.index(target)
            if len(num)> idx+len(number)-k-len(answer)-1:
                start = idx
                break;
            else:
                data.pop(idx)

        # print('될 수 있는 최대값을 가진 idx',start,num[start])
        answer.append(num[start])
        ans_size+=1
        num= num[start+1:]
    res=''
    for i in answer:
        res +=str(i)
    return res

def solution3(number, k):
    answer = []

    size = len(number)-k

    dp=int(number[0:size])
    for idx in range(size,len(number)):
        case =0
        print("구간 ] ",idx)
        for atom in itertools.combinations(str(dp),size-1):
            # print("".join(list(map(str,atom))))
            case = max(case,int("".join(list(map(str,atom)))))
        case = case*10 +int(number[idx])
        print("현재 dp vs case : {} {}".format(dp,case))
        dp = max(dp, case)
    return dp



def solution3(number, k):
    answer = []

    size = len(number)-k

    dp=int(number[0:size])
    for idx in range(size,len(number)):
        case =0
        print("구간 ] ",idx)
        for atom in itertools.combinations(str(dp),size-1):
            # print("".join(list(map(str,atom))))
            case = max(case,int("".join(list(map(str,atom)))))
        case = case*10 +int(number[idx])
        print("현재 dp vs case : {} {}".format(dp,case))
        dp = max(dp, case)
    return dp


def getResult(answer, num, k):
    while (answer) and (int(answer[len(answer)-1]) < num) and (k > 0):
        answer.pop()
        k-=1
    answer.append(num)
    return answer,k

def solution3(number, k):
    answer = []

    for num in number:
        answer,k = getResult(answer,int(num),k)
        # print("현재 num :  {}, 뺄수있는 잔여 k : {} , answer : {}".format(num,k,answer))

    for _ in range(k):
        answer.pop()
    result=""
    for atom in answer:
        result+=str(atom)

    return result

print(solution3("1924",2))
print(solution3("1231234",3))
print(solution3("4177252841",4))
print(solution3("9999999999",4))
# data ="123423"
# print(max(data.remo))

data = "1231234"
'''
k 3 최대 4개 선택가능
dp      num             res
1       1
2       12
3       123
4       1231
5       1231 2           2312
6       2312 3           3123
7       3123 4           3234


"4177252841"
k 4 최대 6개 선택가능능
dp      num                 res
1       4
...
6       417725
7       417725 2            47725 2         //현재 6개중 5개를 골라 큰값+새로운 값 과 현재 값중 큰걸로 갱신 
8       477252 8            77252 8
9       772528 4            77528 4
10      775284 1            77584 1        
'''

print()