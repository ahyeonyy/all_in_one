from collections import deque

n = int(input())
rock = list(map(int,input().split()))
s = int(input())

visited = [False] * n

def bfs(graph,start_v):
    q = deque()
    q.append(start_v)
    visited[start_v] = True

    while q:
        cur_v = q.popleft()
        right_v = cur_v + graph[cur_v]
        left_v = cur_v -graph[cur_v] 
        if right_v < n and not visited[right_v]:
            q.append(right_v)
            visited[right_v] = True
        if left_v >= 0 and not visited[left_v] :
            q.append(left_v)
            visited[left_v] = True

bfs(rock,s-1)
true_count = sum(visited)
print(true_count)