def solution(board):
    answer = 0
    dp=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    dp[0] = board[0]
    for row in range(len(board)):
        dp[row][0] = board[row][0]

    for row in range(0,len(dp)):
        for col in range(0,len(dp[0])):
            if (row - 1 >= 0) and (col -1 >= 0) and board[row][col] ==1:
                dp[row][col] = min(dp[row][col-1],dp[row-1][col],dp[row-1][col-1])+1

    for i in range(len(dp)):
        temp = max(dp[i])
        answer = max(answer, temp)


    # 앞의 행의 가잗큰값만을 뽑아오므로 이렇게하면안됨
    # answer = max(max(max(dp)),answer)
    return answer*answer



print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[1,1,1],[1,0,1],[1,1,1]]))

# lis = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
# for row in lis[1:4]:
#     print(row[1:4])

'''
실패코드
def solution(board):
    height = len(board)
    width = len(board[0])
    for i in range(min(height,width),0,-1):
        print('검사 길이 : ',i)
        for r in range(0,height):
            if r+i-1 < height:
                for c in range(0,width):
                    # r,c 좌표로 부터 i만큼 거리가 있는 경우에만 만들자
                    if  c+i-1< width:
                        toggle = True
                        for row in board[r:r+i]:
                            if 0 in row[c:c+i]:
                                toggle = False
                        if toggle:
                            return i*i
    return 0

'''

'''
def solution(board):
    answer = 0
    dp=[[0]*len(board[0]) for _ in range(len(board))]
    dp[0] = board[0]
    for row in range(len(board)):
        dp[row][0] = board[row][0]

    for row in range(1,len(dp)):
        for col in range(1,len(dp[0])):
            if board[row][col] ==1:
                dp[row][col] = min(dp[row][col-1],dp[row-1][col],dp[row-1][col-1])+1
    
    for i in range(len(dp)):
        temp = max(dp[i])
        answer = max(answer, temp)
    
    # answer = max(max(max(dp)),answer)
    
    return answer*answer

'''