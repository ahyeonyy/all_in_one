N = 8
n,m = map(int,input().split())

check = []

bw = "BWBWBWBWBW"
wb = "WBWBWBWBWB"
pivotB = [bw,wb,bw,wb,bw,wb,bw,wb]
pivotW = [wb,bw,wb,bw,wb,bw,wb,bw]

for i in range(n):
    check.append(input())
    
rst = float('inf')
for i in range(n-N+1):
    for j in range(m-N+1):
        count = 0
        for p in range(N):
            for q in range(N):
                if check[i+p][j+q] != pivotB[p][q]:
                    count +=1
        rst = min(rst,count)
        count = 0
        for p in range(N):
            for q in range(N):
                if check[i+p][j+q] != pivotW[p][q]:
                    count +=1
        rst = min(rst,count)
print(rst)