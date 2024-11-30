def combination_dp(n,m):
   # DP 테이블 초기화
   dp = [[0] * (n+1) for _ in range(m + 1)]

   # DP 초기 조건 설정 
   for i in range(m + 1):
      dp[i][0] = 1 
      if i <= n:
        dp[i][i] = 1
         
   for i in range(1, m+1):
        for j in range(1, min(i,n)+ 1):
           dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
   return dp[m][n]

T = int(input())
for _ in range(T):
   n,m = map(int,input().split())
   print(combination_dp(n,m))
