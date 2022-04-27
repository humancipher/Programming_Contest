from math import gcd

def extgcd(a,b):
    if b == 0:
        return (a,1,0)
    else:
        (d,x,y) = extgcd(b,a % b)
        return (d,y,x-(a//b)*y)

def GCD(A):
    g = A[0]
    for i in range(1,len(A)):
        g = gcd(g,A[i])
    return g

def main():
    T = int(input())
    NSK = [list(map(int,input().split())) for _ in range(T)]
    Ans = []
    for i in range(T):
        N,S,K = NSK[i][0],NSK[i][1],NSK[i][2]
        S = N - S
        g = GCD(NSK[i])
        N,S,K = N//g, S//g, K//g
        if gcd(K,N) == 1:
            x = extgcd(K,N)[1] * S % N
            Ans.append(x)
        else:
            Ans.append(-1)
    for i in range(T):
        print(Ans[i])

if __name__ == "__main__":
    main()
