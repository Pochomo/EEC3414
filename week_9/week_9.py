def cal_dp(n):
    dp = [[0,0] for _ in range(41)]

    dp[0] = [1, 0]  
    dp[1] = [0, 1]

    for i in range(2, n+1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]


    return dp[n]

n = int(input())
for _ in range(n):
    t = int(input())
    result = cal_dp(t)
    print(result[0], result[1])