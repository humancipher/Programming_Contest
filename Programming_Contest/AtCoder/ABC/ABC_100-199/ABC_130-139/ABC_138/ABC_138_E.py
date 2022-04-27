from bisect import bisect_left
INF = 10**6

S = input()
T = input()
Al = [[] for _ in range(26)]
for i in range(len(S)):
    Al[ord(S[i])-ord("a")].append(i+1)
for i in range(26):
    Al[i].append(INF)

possibile = True
for i in range(len(T)):
    if len(Al[ord(T[i])-ord("a")]) == 1:
        possibile = False            
        break
if possibile:
    sho,amari = 0,0
    for i in range(len(T)):
        pt = bisect_left(Al[ord(T[i])-ord("a")],amari+1)
        if Al[ord(T[i])-ord("a")][pt] == INF:
            sho += 1
            amari = Al[ord(T[i])-ord("a")][0]
        else:
            amari = Al[ord(T[i])-ord("a")][pt]
    ans = sho * len(S) + amari
else:
    ans = -1
print(ans)
