import itertools
def solution(orders, course):
    answer = []
    # cnt_combi =[0 for _ in range(len(orders))]
    # total =set()
    # for i in range(len(orders)):
    #     # print(set(list(orders[i])))
    #     tmp =set(list(orders[i]))
    #     cnt_combi[i] = tmp
    #     total = total| tmp
    #
    # print('집합분리',cnt_combi)
    # total = list(total)
    # print('총 문자합',total)




    for cnt in course:
        targets=[]
        # 해당 course의 combinition 값을 target로 만듦
        for order in orders:
            for target in list(itertools.combinations(set(order),cnt)):
                targets.append(target)

        # print(targets)
        # print('fun--------------------------------')
        results = getMaxMenu(orders,targets)
        for result in results:
            answer.append(result)

    answer.sort()
    return answer

#origin을 target으로 검사 -> 가장 큰값을 반환 그러나 큰값이 여러개면 같이 반환
def getMaxMenu(origins,targets):

    result =dict()
    for target in targets:
        target = set(target)
        cnt = 0
        # print('target으로 비교 시작',target)
        for origin in origins:
            # print('->대상 :',origin)
            origin = set(origin)
            if target == origin.intersection(target):
                cnt+=1

        if cnt > 1 :
            target = list(target)
            target.sort()
            result[''.join(target)]= cnt

    # print('결과',result)
    # key = max(result,key=result.get)
    # val = max(result.values())
    # print('큰값:',val)
    output = [keys for keys,v in result.items() if max(result.values())== v  ]
    # print('아웃:',output)
    return output
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

# datas = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
#
# for data in datas:
#     #원소분리
#     print(set(list(data)))