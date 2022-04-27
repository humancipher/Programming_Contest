from math import sqrt

A,B = map(int,input().split())

def gcd(a,b):
    if a < b:
        a,b = b,a
    while a % b != 0:
        r = a % b
        a,b = b,r
    return b

def count_prime(n):
    #nを割り切る素数の個数
    if n == 1:
        return 0
    n_is_prime = True
    P = []
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            n_is_prime = False
            P.append(i)
            while n % i == 0:
                n //= i
    if n_is_prime:
        return 1
    elif n == 1:
        return len(P)
    else:
        #この時点で割り切れずに残ったnは未発見の素数
        return len(P)+1

g = gcd(A,B)
c_p = count_prime(g)
print(c_p+1)
