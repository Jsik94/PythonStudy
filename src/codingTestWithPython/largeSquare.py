def solution(board):
    dp=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    dp[0] = board[0].copy()
    for row in range(len(board)):
        dp[row][0] = board[row][0]
    print(dp)

    for row in range(0,len(dp)):
        for col in range(0,len(dp[0])):
            if (row - 1 > 0) and (col -1 > 0):
                dp[row][col] = min(dp[row][col-1],dp[row-1][col],dp[row-1][col-1])+1

    return 0



print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))

# lis = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
# for row in lis[1:4]:
#     print(row[1:4])

