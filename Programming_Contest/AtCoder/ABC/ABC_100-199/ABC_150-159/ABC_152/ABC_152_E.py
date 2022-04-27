from math import gcd
from functools import reduce

def LCM(A):
    return reduce(lambda a,b: (a * b) // gcd(a,b), A)

def inv(a,p):
    return pow(a,p-2,p)

def solve(A,N):
    #B[i] = LCM(A)//A[i]
    ans = 0
    L = LCM(A)
    mod = 10**9+7
    for i in range(N):
        b = L * inv(A[i],mod)
        b %= mod
        ans += b
        ans %= mod
    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(solve(A,N))

if __name__ == "__main__":
    main()
