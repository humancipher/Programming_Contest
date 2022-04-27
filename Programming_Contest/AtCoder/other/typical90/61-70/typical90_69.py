mod = 10**9+7
n,k = map(int,input().split())
ans = 1
if n == 1:
    ans *= k
elif n == 2:
    ans *= k
    ans *= (k-1)
    ans %= mod
else:
    ans *= k
    ans *= (k-1)
    ans %= mod
    ans *= pow(k-2,n-2,mod)
    ans %= mod
print(ans)