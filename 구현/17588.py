n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))
check_list = [i for i in range(1,max(num_list))]

for j in num_list:
    if j in check_list:
        check_list.remove(j)
if check_list:
    for n in check_list:
        print(n)
else:
    print("good job")