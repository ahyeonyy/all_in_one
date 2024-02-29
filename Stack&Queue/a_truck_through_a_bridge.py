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
