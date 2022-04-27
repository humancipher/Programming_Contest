mod = 10**9+7

n = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))

T2 = [[T[i],T[i]] for i in range(n)] #T2[i]  [i番目の山の高さの[最小,最大]]
A2 = [[A[i],A[i]] for i in range(n)] #A2[i]  [i番目の山の高さの[最小,最大]]
for i in range(n-1):
    if T[i+1] == T[i]:
        T2[i+1][0] = 1
for i in reversed(range(1,n)):
    if A[i-1] == A[i]:
        A2[i-1][0] = 1
ans = 1
for i in range(n):
    ans *= (min(T2[i][1],A2[i][1]) - max(T2[i][0],A2[i][0]) + 1)
    if ans < 0:
        ans = 0
        break
    ans %= mod
print(ans)