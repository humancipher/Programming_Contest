from math import sqrt

def eratos(n):
    P = [True for _ in range(n+1)]
    for i in range(2,int(sqrt(n))+1):
        if P[i]:
            for j in range(2,n//i + 1):
                P[i*j] = False
    Ans = []
    for i in range(2,n+1):
        if P[i]:
            Ans.append(i)
    return Ans

def main():
    n,k = map(int,input().split())
    P = eratos(n)
    C = [0 for _ in range(n+1)]
    for i in range(len(P)):
        for j in range(1,n//P[i]+1):
            C[P[i]*j] += 1
    ans = 0
    for i in range(n+1):
        if C[i] >= k:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
