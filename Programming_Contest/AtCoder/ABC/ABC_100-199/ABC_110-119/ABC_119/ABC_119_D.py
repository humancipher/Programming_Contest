from bisect import bisect_left
INF = 10**11
a,b,q = map(int,input().split())
S = [int(input()) for _ in range(a)]
T = [int(input()) for _ in range(b)]
X = [int(input()) for _ in range(q)]
S.append(INF)
T.append(INF)
S = [-INF] + S
T = [-INF] + T

Ans = []
for x in X:
    ps = bisect_left(S,x)
    pt = bisect_left(T,x)
    pat1 = max(S[ps],T[pt]) - x
    pat2 = x - min(S[ps-1],T[pt-1])
    pat3 = x - S[ps-1] + 2*(T[pt]-x)
    pat4 = 2 * (x - S[ps-1]) + T[pt] - x
    pat5 = S[ps] - x + 2*(x - T[pt-1])
    pat6 = 2*(S[ps] - x) + x - T[pt-1] 
    ans = min(pat1,pat2,pat3,pat4,pat5,pat6)
    Ans.append(ans)
for i in range(q):
    print(Ans[i])