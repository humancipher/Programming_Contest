n = int(input())
V = dict()
for _ in range(n):
    s = input()
    if s not in V:
        V[s] = 1
    else:
        V[s] += 1

cnt = 0
for s in V:
    if V[s] > cnt:
        ans = s
        cnt = V[s]
print(ans)