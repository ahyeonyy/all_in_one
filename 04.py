def max_gold_tickets(tickets_str, roll, shop, money):
    # 티켓 정보를 딕셔너리로 변환
    tickets = {}
    for ticket_str in tickets_str:
        name, price = ticket_str.split()
        tickets[name] = int(price)

    # DP 테이블 초기화
    n = len(shop)
    m = money
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(n + 1)]

 # DP 계산
    for i in range(1, n + 1):  # 상점
        for j in range(money + 1):  # 자금
            for k in range(n + 1):  # 새로고침 횟수
                # 새로고침
                if j >= roll and k < n:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - roll][k + 1])

                # 티켓 구매 (수정된 부분)
                for c in shop[i - 1]:
                    price = tickets[c]
                    if j >= price:
                        # 해당 티켓을 최대한 많이 구매하고, 남은 자금으로 다른 티켓을 구매하는 경우도 고려
                        max_buy = min(j // price, shop[i - 1].count(c))
                        gold = max_buy // 3
                        for buy in range(max_buy + 1):
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - price * buy][k] + gold)

    return dp[n][money][n]

def get_gold(char, tickets):
    # 일반 티켓 3개를 황금 티켓 1개로 교환 가능한 경우 황금 티켓 개수 반환
    count = tickets[char]
    return count // 3

# 예시
tickets_str = ["A 2", "B 1"]
roll = 5
shop = [["A", "A", "A"], ["A", "B", "B"], ["A", "B", "B"], ["A", "B", "B"]]
money = 19

result = max_gold_tickets(tickets_str, roll, shop, money)
print(result)  # 최대 황금 티켓 개수 출력