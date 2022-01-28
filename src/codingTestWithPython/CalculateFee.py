from datetime import datetime
import math
def solution(fees, records):
    answer = []
    total = list();
    time_data = dict();
    res = dict();
    list_ = list();
    for record in records:
        date_str,num,status = record.split(' ')
        # date_str = datetime.strptime(date_str, '%H:%M')
        list_.append([num,date_str,status])

    list_.sort(key=lambda x: (x[0],x[1]))
    # for lst in list_:
    #     print(lst)
    for lst in list_:
        # print(res.get(lst[0],True))
        if not res.get(lst[0],False):
            res[lst[0]] = datetime.strptime(lst[1], '%H:%M')
        else :
            latency = int((datetime.strptime(lst[1], '%H:%M') - res[lst[0]]).seconds/60)
            time_data[lst[0]] = latency if not time_data.get(lst[0],False) else time_data[lst[0]]+latency
            del res[lst[0]]

    # print("<---->")
    # 요금 계산
    for key, value in res.items():
        # print(key,'-',value)
        latency = int((datetime.strptime("23:59", '%H:%M') - res[key]).seconds/60)
        time_data[key] = latency if not time_data.get(key,False) else time_data[key]+latency


    # print("<---->")
    # 요금 계산
    for key, value in time_data.items():
        print(key,'-',value)

        extra_fee = math.ceil((value-fees[0])/fees[2])*fees[3]

        total.append([key,fees[1]+ (extra_fee if (value-fees[0])>=0 else 0)])

    total.sort(key=lambda x:x[0])
    # print(total)
    while total:
        d = total.pop(0)[1]
        # print(d)
        answer.append(d)
    return answer


print(solution([180, 5000, 10, 600],["05:34 5961 IN", "18:59 0000 IN", "19:09 0148 OUT", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "22:59 5961 IN", "23:00 5961 OUT"]))