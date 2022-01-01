import copy
import itertools

def solution(n, weak, dist):
    answer = -1
    dist.sort(reverse=True)
    print("점검의 모든 경우의 수")
    orders_weak = list(itertools.permutations(weak,len(weak)))
    print(orders_weak)
    print(len(orders_weak))
    print("모든 dist의 수")
    orders_dist = list(itertools.permutations(dist,len(dist)))
    print(len(orders_dist))
    print(orders_dist)

    #dist 인원을 기준으로 구해보자
    res =9999
    #특정 dist set을 기준으로
    # for kind_dist in orders_dist:
        #테스팅할 weak order를 가져옴
    for kind_weak in orders_weak:
        tmp = list(copy.deepcopy(kind_weak))
        #해당 dist set을 하나씩 더하며 갈 수 있는지 확인
        for i in range(len(dist)):
            standard = tmp.pop(0)
            if not tmp:
                res =min(res,i+1)
                break
            else:
                # start = standard-kind_dist[i] if standard-kind_dist[i] <0 else standard-kind_dist[i] + 12
                # end = standard+kind_dist[i] if standard+kind_dist[i] <12 else standard+kind_dist[i] - 12
                ran =[standard]
                for k in range(1,dist[i]+1):
                    ran.append(ran[0]+k if ran[0]+k < 12 else ran[0]+k-12)

                # print(standard,'-',kind_dist[i],': ',ran)
                toggle =False
                while True:
                    if tmp and tmp[0] in ran:
                        tmp.pop(0)
                        toggle = True
                    else:
                        if not toggle:
                            #다시 삽입
                            tmp.insert(0,standard)
                        break

                print("남은 것들",tmp)
                if not tmp :
                    res =min(res,i+1)
                    break

        print("weak set 결과 :" ,res)

    return res

#
# #원형에서 첫번째 기준으로 왼쪽으로 second까지 순차거리
# # second ~ first 내에 있는 값
# def cir_len(first,second,n):
#     result = first -second
#     return int(result if result > 0 else n+result)
#
#
# def total_len(arr,n):
#     dist = 0
#     if len(arr)<2:
#         return 0
#     print(arr)
#     print(len(arr),arr[0],arr[1])
#     for i in range(1,len(arr)):
#         dist+= cir_len(arr[i-1],arr[i],n)
#         # print(arr[i-1],arr[i])
#         # pass
#
#     print(arr,"왼쪽으로 순차 진행시 거리 : " ,dist)
#     return dist
#
#
#
# print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))

# list_=[1]
# print(type([1]),list_.pop(0),list_)
