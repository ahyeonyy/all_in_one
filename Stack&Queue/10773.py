import sys
K = int(sys.stdin.readline().strip())
stack = []
for _ in range(K):
    i = int(sys.stdin.readline().strip())
    if i != 0 :
        stack.append(i)
    else : 
        stack.pop()
print(sum(stack))