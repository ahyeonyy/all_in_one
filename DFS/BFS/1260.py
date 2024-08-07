from collections import deque

# 입력 받기
n, m, v = map(int, input().split())

# 그래프 초기화
graph = {i: [] for i in range(1, n + 1)}

# 그래프에 간선 추가
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS 함수 정의
def dfs(cur_v, visited):
    visited.append(cur_v)
    for v in sorted(graph[cur_v]):
        if v not in visited:
            dfs(v, visited)

# BFS 함수 정의
def bfs(start_v):
    visited = []
    queue = deque([start_v])
    while queue:
        cur_v = queue.popleft()
        if cur_v not in visited:
            visited.append(cur_v)
            for v in sorted(graph[cur_v]):
                if v not in visited:
                    queue.append(v)
    return visited

# DFS 탐색
dfs_visited = []
dfs(v, dfs_visited)

# BFS 탐색
bfs_visited = bfs(v)

# 결과 출력
print(' '.join(map(str, dfs_visited)))
print(' '.join(map(str, bfs_visited)))
