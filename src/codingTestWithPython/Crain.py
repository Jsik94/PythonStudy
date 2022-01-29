def solution(board, moves):
    answer = 0
    res = []
    # print(rotated(board))
    board = rotated(board)

    for lst in board:
        while 0 in lst :
            lst.remove(0)

    for lst in board:
        print(lst)

    for move in moves:
        # print(board[move-1])
        if len(board[move-1]) ==0 : continue
        data = board[move-1].pop()
        #
        print('현재 결과 :' ,res, ' 현재 꺼낸 값 ', data)
        if not res :
            res.append(data)
        else:
            if res[len(res)-1] != data:
                res.append(data)
            else:
                answer+=2;
                res.pop()
    # print("result",res)
    return answer


def myPop(arr):
    data=0
    for i in range(len(arr),0,-1):
        if arr[i-1] == 0:
            continue
        else :
            data = arr[i-1]
            arr[i-1]=0
            break;
    return data

def rotated(a):
    n = len(a)
    m = len(a[0])
    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

result =solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]);
print(result)