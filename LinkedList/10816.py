N = int(input()) # 상근이가 가지고 있는 숫자 카드의 수 

num_card = list(map(int, input().split()))
num_dict = {}
for i in num_card:
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] += 1

M = int(input())
guess = list(map(int,input().split()))

answer = []
for n in guess:
    if n in num_dict:
        answer.append(num_dict[n])
    else:
        answer.append(0)

print(' '.join(map(str, answer)))