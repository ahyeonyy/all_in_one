N = int(input())
w = ''

cnt = 0
for _ in range(N):
    alpha = []
    word = input()
    for i in word : 
        if i != w and (i not in alpha) : 
            w = i
            alpha.append(i)
        elif i == w  :
            continue
        elif i != w and (i in alpha) :
            w = i
            cnt = 0
            break
    cnt +=1
print(cnt)
