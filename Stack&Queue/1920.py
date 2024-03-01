import sys 
N = int(sys.stdin.readline().strip())
a = sys.stdin.readline().strip()
a_list = map(int, a.split())
dic = {}
for i in a_list :
    if i not in dic:
        dic[i] = i
M = int(sys.stdin.readline().strip())
b = sys.stdin.readline().strip()
b_list = map(int, b.split())

for n in b_list :
    if n in dic :
        print(1)
    else:
        print(0)