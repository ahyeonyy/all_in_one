def count_ways(n, m, k):
    # DP 테이블 초기화
    dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    
    # 초기 상태: 구슬을 모두 잃지 않으면서 시작 (0번 게임 후)
    dp[n][m][0] = 1
    
    for games_left in range(k):
        for i in range(n + 1):
            for j in range(m + 1):
                if dp[i][j][games_left] > 0:
                    # 승리하는 경우
                    if i > 0 and j < m:
                        dp[i - 1][j + 1][games_left + 1] += dp[i][j][games_left]
                    # 패배하는 경우
                    if j > 0 and i < n:
                        dp[i + 1][j - 1][games_left + 1] += dp[i][j][games_left]

    # 최종 결과: 게임이 끝나고 한 명이 모든 구슬을 잃은 경우의 수를 계산
    result = 0
    for i in range(1, n + 1):
        result += dp[i][0][k]
    for j in range(1, m + 1):
        result += dp[0][j][k]
    
    return result

# 입력 받기
n, m, k = map(int, input().split())

# 함수 호출 및 결과 출력
print(count_ways(n, m, k))
