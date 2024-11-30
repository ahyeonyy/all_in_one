from collections import deque

T = int(input())


N, M, K = map(int(),input().split())

farm = [[0] * M for _ in range(N)]

for k in range(K) :
    x,y = map(int(), input().split())
    farm[x][y] = 1

print(farm)