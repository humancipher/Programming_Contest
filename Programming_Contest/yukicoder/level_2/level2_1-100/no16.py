x,n = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**6+3

ans = 0
for a in A:
    ans += pow(x,a,mod)
    ans %= mod
print(ans)
