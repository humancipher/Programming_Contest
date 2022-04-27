def cal(n,t):
    _n,_t,digit,ans = n,t,0,0
    while _n > 0 and _t > 0:
        if _n % 2 == 1:
            if 2**(digit+1)-1 <= t:
                ans += 2**digit
            else:
                ans += t - 2**digit + 1
        _n //= 2
        _t //= 2
        digit += 1
    return ans

n,l,r = map(int,input().split())
print(cal(n,r)-cal(n,l-1))
