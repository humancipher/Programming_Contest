from math import gcd

def Prime(n):
    P = [True for _ in range(n+1)]
    P[0],P[1] = False,False
    Ans = list()
    for i in range(2,n+1):
        if P[i]:
            Ans.append(i)
            for j in range(2,n//i+1):
                P[i*j] = False
    return Ans

def solve(A,N):
    P = Prime(50)
    ans = 10**20
    for i in range(1,2**len(P)):
        tmp = 1
        for j in range(len(P)):
            if i & 2**j:
                tmp *= P[j]
        kouho = True
        for k in range(N):
            if gcd(A[k],tmp) == 1:
                kouho = False
                break
        if kouho:
            ans = min(ans,tmp)
    return ans
    
def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(solve(A,N))

if __name__ == "__main__":
    main()
