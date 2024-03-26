N = int(input())

for i in range(N):
    total_sum = i +sum(map(int,str(i)))
    if total_sum == N :
        print(i)
        break
else:
        print(0)
    