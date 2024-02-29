
N = int(input())
stack = []
for i in range(N) :
    command = input()
    if command.startswith("push"):
        a = command.split()
        stack.append(a[1])
    elif command == "pop" : 
        if stack :
            print(stack[-1])
            stack.pop()
        else : 
            print(-1)
    elif command == "top" :
        if stack :
            print(stack[-1])
        else : 
            print(-1)
    elif command == "size" : 
        print(len(stack))
    elif command == "empty" :
        if stack :
            print(0)
        else :
            print(1)