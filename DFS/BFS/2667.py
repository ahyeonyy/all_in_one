from collections import deque

# 입력 받기
n = int(input()) # 지도의 크기
grid = [] # 지도가 들어갈 리스트 초기화
# 지도 입력 받기
for _ in range(n):
    c = [int(n) for n in input()]
    grid.append(c)

total = []
# BFS 방문 체크 초기화 
visited = [[False] * n for _ in range(n)]

def complex(grid):
    def bfs(x, y):
        # 이동 좌표 
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        visited[x][y] = True
        queue = deque([(x, y)])
        cnt = 0
        while queue:
            cur_x, cur_y = queue.popleft()
            cnt += 1
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if 0 <= next_x < n and 0 <= next_y < n:
                    if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))  # 수정된 부분
        return cnt

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                total.append(bfs(i, j))

    return total
answer = complex(grid)
print(len(answer))
answer.sort()
for c in answer:
    print(c)
