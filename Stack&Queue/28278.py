import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N) :
    i = sys.stdin.readline().strip()
    if i.startswith("1"):
        n = i.split()
        stack.append(n[1])
    elif i == ("2") :
        if stack :
            print(stack.pop())
        else:
            print(-1)
    elif i == ("3"):
        print(len(stack))
    elif i == ("4"):
        if stack : 
            print(0)
        else:
            print(1)
    elif i == ("5"):
        if stack :
            print(stack[-1])
        else :
            print(-1)