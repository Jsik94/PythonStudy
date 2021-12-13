#   Link
#   https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    pattern2 = [1,3,4,5]
    pattern3 = [3,1,2,4,5]
    result =[0]*3
    person = [[] for k in range(0,3)]

    for i in range(1,len(answers)+1) :
        person[0].append(i % 5 if i % 5 != 0 else 5)
        person[1].append(2 if i % 2 == 1 else pattern2[int((i / 2) % len(pattern2)) - 1])
        person[2].append(pattern3[int(i / 2) % len(pattern3)] if i % 2 == 1 else person[2][i - 2])

    for i in range(0,3) :
        for k in range(0,len(answers)):
            if person[i][k] == answers[k] :
                result[i] = result[i]+1;

    answer = [i+1 for i in range(0,3) if result[i] == max(result)]

    return answer


