def fibo(n):
    # 호출 횟수를 저장할 변수들
    cnt0 = [0] * (n + 1)
    cnt1 = [0] * (n + 1)

    # 피보나치 초기값
    dp = [0] * (n + 1)
    
    dp[0] = 0
    cnt0[0] = 1  # dp[0]은 1회 호출
    
    if n > 0:
        dp[1] = 1
        cnt1[1] = 1  # dp[1]은 1회 호출
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        cnt0[i] = cnt0[i - 1] + cnt0[i - 2]  # dp[0] 호출 횟수 누적
        cnt1[i] = cnt1[i - 1] + cnt1[i - 2]  # dp[1] 호출 횟수 누적

    return dp[n], cnt0[n], cnt1[n]

n = int(input())
for _ in range(n):
    x = int(input())
    _, cnt0, cnt1 = fibo(x)
    print(cnt0, cnt1)
