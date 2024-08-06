N = int(input()) # 상근이가 가지고 있는 숫자 카드의 수 

num_card = list(map(int, input().split()))
num_dict = {num : True for num in num_card}
M = int(input())
guess = list(map(int,input().split()))

answer = [1 if n in num_dict else 0 for n in guess]

print(' '.join(map(str, answer)))