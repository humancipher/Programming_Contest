from bisect import bisect_left

INF = 10**6
n,k = map(int,input().split())
S = input()

Al = [[] for _ in range(26)]
for i in range(n):
    Al[ord(S[i])-ord("a")].append(i)
for i in range(26):
    Al[i].append(INF)

pt,Ans = -1,[]
while len(Ans) < k:
    for i in range(26):
        tmp = bisect_left(Al[i],pt+1)
        if n-Al[i][tmp] >= k-len(Ans):
            pt = Al[i][tmp]
            Ans.append(S[pt])
            break
print("".join(Ans))