n , m = map(int,input().split())
n_list = [x for x in range(1,n+1)]
for _ in range(m):
    i , j = map(int,input().split())
    k = n_list[j-1]
    n_list[j-1] = n_list[i-1]
    n_list[i-1] = k
for e in n_list:
    print(e, end= " ")