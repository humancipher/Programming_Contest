from math import gcd

def solve(A,N):
    L,R = [A[0]],[A[-1]] #L[i]:右からGCD(A[:i+1]),R[i]:GCD[N-i-1:]
    for i in range(N-1):
        L.append(gcd(L[-1],A[i+1]))
        R.append(gcd(R[-1],A[N-i-2]))
    
    ans = max(L[-2],R[-2])
    for i in range(N-2):
        ans = max(ans,gcd(L[i],R[N-3-i]))
    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))

    print(solve(A,N))

if __name__ == "__main__":
    main()
