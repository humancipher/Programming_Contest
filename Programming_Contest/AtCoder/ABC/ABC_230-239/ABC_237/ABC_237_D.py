from collections import deque

n = int(input())
S = input()
D = deque()
D.append(n)
for i in reversed(range(n)):
    if S[i] == "R":
        D.appendleft(i)
    else:
        D.append(i)
D = list(D)
print(" ".join(map(str,D)))