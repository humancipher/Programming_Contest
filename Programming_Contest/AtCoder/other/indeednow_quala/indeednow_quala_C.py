n = int(input())
S = [int(input()) for _ in range(n)]
S.append(0)
S.sort(reverse=True)
q = int(input())
K = [int(input()) for _ in range(q)]
Ans = []
for i in range(q):
    if S[K[i]] == 0:
        Ans.append(0)
    else:
        Ans.append(S[K[i]]+1)
for i in range(q):
    print(Ans[i])