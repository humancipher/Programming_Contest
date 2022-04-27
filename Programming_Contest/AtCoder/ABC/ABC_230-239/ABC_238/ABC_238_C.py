mod = 998244353
n = int(input())
upper = 10
ans = 0
while True:
    if upper-1 <= n:
        tmp = upper - (upper//10)
        ans += tmp*(tmp+1)//2
        ans %= mod
        upper *= 10
    else:
        tmp = n - (upper//10) + 1
        ans += tmp*(tmp+1)//2
        ans %= mod
        break
print(ans)