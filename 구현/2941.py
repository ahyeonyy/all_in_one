import re
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
n = 0
for c in croatia:
    if c in word:
        print(word,",",c)
        word = re.sub()
        n+=1
print(n+len(word))
