from sys import stdin
from collections import deque
N = int(stdin.readline())
queue = deque()
for _ in range(N) :
    command = stdin.readline().strip()
    if command.startswith("push") :
        queue.append(command.split()[1])
    elif command == "pop" :
        if queue :
            print(queue.popleft())
        else :
            print(-1)
    elif command == "size" :
        print(len(queue))
    elif command == "empty" :
        if queue :
            print(0)
        else :
            print(1)
    elif command == "front" : 
        if queue :
            print(queue[0])
        else :
           print(-1)
    elif command == "back" :
        if queue :
            print(queue[-1])
        else :
           print(-1)