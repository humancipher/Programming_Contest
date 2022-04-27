m,n = map(int,input().split())
BIGNUM = 10**9+7

def power(m,n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return (m * power(m**2 % BIGNUM,n//2)) % BIGNUM
    else:
        return power(m**2 % BIGNUM,n//2) % BIGNUM

print(power(m,n))
