N = int(input())
S = list(input())

ans = 0
for i in range(1,N-1):
    S1,S2 = set(S[:i]),set(S[i:])
    ans = max(ans,len(S1 & S2))

print(ans)
