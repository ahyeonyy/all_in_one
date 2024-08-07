n = int(input())  # 전체 사람의 수
p1, p2 = map(int, input().split())  # 촌수 계산해야 하는 서로 다른 두 사람
m = int(input())  # 부모 자식들 간의 관계 개수

# 빈 그래프 초기화
graph = {i: [] for i in range(1, n + 1)}

# 부모-자식 관계를 그래프에 추가
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

visited = [False] * (n + 1)  # 방문 여부 확인 리스트
cnt = -1  # 촌수 카운트 초기화

def dfs(cur_v, target, count):
    global cnt
    visited[cur_v] = True
    
    if cur_v == target:
        cnt = count
        return

    for neighbor in graph[cur_v]:
        if not visited[neighbor]:
            dfs(neighbor, target, count + 1)

# DFS 탐색 시작
dfs(p1, p2, 0)

print(cnt)
