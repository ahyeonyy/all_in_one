N = int(input())
stair = []
for _ in range(N):
    x = int(input())
    stair.append(x)

if N == 1:
    print(stair[0])
    exit()

dp = [0] * N

# 초기 조건 설정
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]

if N > 2:
    dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])

# 점화식으로 DP 배열 채우기
for i in range(3, N):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[N-1])
