def solution(s):
    stack = []
    for i in s :
        if i == "(" :
            stack.append(")")
        elif stack and i == ")" :
            print("여기당!")
            stack.pop()
    return stack

solution("(())")