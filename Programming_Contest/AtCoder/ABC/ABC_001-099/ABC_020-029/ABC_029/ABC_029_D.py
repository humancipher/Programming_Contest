from math import ceil

def cal(n):
    n0= 1
    ans = 0
    while n0 <= n:
        if n // n0 > 1:
            if (n // n0) % 10 != 1:
                ans += ceil((n - n % n0)/(n0*10)) * n0
            else:
                ans += ((n - n % n0)//(n0*10)) * n0
                ans += n  % n0 + 1
        else:
            ans += (n % n0) + 1
        n0 *= 10
    return ans

n = int(input())
print(cal(n))