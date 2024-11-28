def check(perm, signs):
    for i in range(len(signs)):
        if signs[i] == '<' and perm[i] > perm[i+1]:
            return False
        if signs[i] == '>' and perm[i] < perm[i+1]:
            return False
    return True

def backtrack(index, perm, signs, used, max_num, min_num):
    if index == len(signs) + 1:
        if check(perm, signs):
            num = ''.join(map(str, perm))
            max_num[0] = max(max_num[0], num)
            min_num[0] = min(min_num[0], num)
        return

    for i in range(10):
        if not used[i]:
            used[i] = True
            perm.append(i)
            backtrack(index + 1, perm, signs, used, max_num, min_num)
            perm.pop()
            used[i] = False

def find_min_max(signs):
    max_num = ['']
    min_num = ['9999999999']  # 임의의 큰 수로 초기화
    used = [False] * 10

    backtrack(0, [], signs, used, max_num, min_num)

    return max_num[0], min_num[0]

# 입력 처리
k = int(input())  # 부등호 문자의 개수 입력
signs = input().split()  # 부등호 기호들을 리스트로 입력 받음

# 최댓값과 최솟값 찾기
max_value, min_value = find_min_max(signs)

# 결과 출력
print( max_value)
print( min_value)
