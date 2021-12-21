def solution(s):
    answer = ""
    start =0
    i = -1
    print("r")
    while i+1 < len(s):
        i += 1
        # 숫자가 발생하면 그전까지의 값을 전환
        if s[i].isdigit():
            answer= answer+transNum(s[start:i])
            answer= answer+ s[i]
            start = i+1

    if len(answer) !=len(s):
        answer += transNum(s[start:i+1])

    return answer

def transNum(words):
    dic = {"zero":"0","one":"1","two":"2","three":"3","four":"4",
          "five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    res =""
    idx =0
    print("단어 : " ,words)
    for i in range(2,len(words)+1) :
        word = words[idx:i]
        if words[idx:i] in dic :
            print("존재함!")
            res += dic[words[idx:i]]
            idx = i

    print("리턴 : ",res)
    return res


print(solution("one4seveneight"))