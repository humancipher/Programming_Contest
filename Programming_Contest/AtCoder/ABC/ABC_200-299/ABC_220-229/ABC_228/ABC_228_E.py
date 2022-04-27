mod = 998244353
n,k,m = map(int,input().split())
#ans = m**(k**n)
#gcd(a,p) == 1 -> pow(a,p-1,p) == 1
if m % mod == 0:
    print(0)
else:
    sisu = pow(k,n,mod-1)
    ans = pow(m,sisu,mod)
    print(ans)