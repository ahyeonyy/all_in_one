<<<<<<< HEAD
def solution(bridge_length, weight, truck_weights):
    stack = []
    for t in truck_weights :
        stack.append(t)
        if sum(stack) > weight :
            stack.pop()
        answer += bridge_length
    answer = 0
    return answer

solution(2,100,[7,4,5,6])
=======
from collections import deque

def solution(bridge_length, weight, truck_weights):
    stack = deque()    
    answer = 0
    while len(truck_weights):
        stack.append()
    return answer

solution(2,10,[7,4,5,6])
>>>>>>> cc25163 (10828 시간초과)
