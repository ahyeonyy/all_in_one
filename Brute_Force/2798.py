from itertools import combinations

N, M = map(int,input().split())
num_list = list(map(int,input().split()))
arr = []
for card in combinations(num_list,3):
    if sum(card) <= M :
        arr.append(sum(card))
print(max(arr))