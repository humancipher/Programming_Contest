from math import gcd

def Eratos(n): #n以下の素数の集合
    M = [True for _ in range(n+1)]
    p = 2
    while p**2 <= n:
        if M[p]:
            for i in range(2,n // p + 1):
                M[p * i] = False
        p += 1

    ans = []
    for i in range(2,n+1):
        if M[i]:
            ans.append(i)
    return ans

def fast_fact_prev(n,P):
    D = [i for i in range(n+1)]
    for i in range(len(P)):
        if P[i] * 2 > n:
            break
        else:
            for j in range(2, n // P[i] + 1):
                D[P[i] * j] = min(D[P[i] * j],D[P[i]])
    return D

def fast_fact(n,D):
    ans = set()
    while n > 1:
        ans.add(D[n])
        if n != D[n]:
            n //= D[n]
        else:
            ans.add(n)
            break
    return ans

def GCD(A):
    if len(A) == 1:
        return A[0]
    else:
        g = gcd(A[0],A[1])
        for i in range(2,len(A)):
            g = gcd(g,A[i])
            if g == 1:
                break
        return g

def main():
    N = int(input())
    A = list(map(int,input().split()))

    maxA = max(A)
    Prime = Eratos(maxA)
    Prev = fast_fact_prev(maxA,Prime)
    C = set()
    Pat = ["pairwise coprime","setwise coprime","not coprime"]
    ans = 0
    for i in range(N):
        A_insu = fast_fact(A[i],Prev)
        for a in A_insu:
            if a not in C:
                C.add(a)
            else:
                ans = 1
                break
    
    if ans == 1:
        if GCD(A) > 1:
            ans = 2
    
    print(Pat[ans])

if __name__ == "__main__":
    main()

