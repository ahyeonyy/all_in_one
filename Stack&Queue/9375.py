from sys import stdin
N = int(stdin.readline())
for _ in range(N):
    n = int(stdin.readline())
    for _ in range(n):
        name, types  = map(str,stdin.readline().strip().split())
#  이름과 종류 나눠서 저장 