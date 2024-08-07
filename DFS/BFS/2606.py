n = int(input()) # 컴퓨터의 수 
m = int(input()) # 연결된 컴퓨터의 수 

graph = {i : [] for i in range(1,n+1)}

for _ in range(m) :
    x,y = map(int,input().split()) 
    graph[x].append(y)
    graph[y].append(x)

visited = []
def dfs(virus):
    visited.append(virus)
    for v in graph[virus]:
        if v not in visited :
            dfs(v)
    return len(visited) -1 
print(dfs(1))
