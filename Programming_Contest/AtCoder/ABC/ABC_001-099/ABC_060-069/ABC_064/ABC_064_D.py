from itertools import accumulate

N = int(input())
S = input()

C = [0 for i in range(N)]

for i in range(N):
    if S[i] == "(":
        C[i] = 1
    else:
        C[i] = -1

CR = list(accumulate(C))

l_hosei = 0
for i in range(N):
    l_hosei = max(l_hosei,-CR[i])

C = [1] * l_hosei + C

CR = list(accumulate(C))

r_hosei = max(CR[-1],0)

C = C + [-1] * r_hosei

ans = ""
for i in range(len(C)):
    if C[i] == 1:
        ans += "("
    else:
        ans += ")"

print(ans)
