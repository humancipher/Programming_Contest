n,k = map(int,input().split())
S = [input() for _ in range(n)]

ans = 0
for i in range(2**n):
    Al = [0 for _ in range(26)]
    for j in range(n):
        if i & 2**j:
            for t in range(len(S[j])):
                Al[ord(S[j][t])-ord("a")] += 1
    cnt = 0
    for t in range(26):
        if Al[t] == k:
            cnt += 1
    ans = max(ans,cnt)
print(ans)