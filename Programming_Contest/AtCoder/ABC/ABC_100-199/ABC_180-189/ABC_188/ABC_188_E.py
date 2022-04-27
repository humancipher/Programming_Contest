from queue import Queue

INF = 1 << 60

def solve(A,XY,N,M):
    Child = [set() for _ in range(N+1)] #街iから1回でいける街の集合
    for x,y in XY:
        Child[x].add(y)

    Money = [INF for _ in range(N+1)] #M[i] = [街iの直前までのパスで最小の買値]
    
    for p in range(1,N+1):
        for c in Child[p]:
            Money[c] = min(Money[c],Money[p],A[p])
    
    ans = -INF
    for i in range(1,N+1):
        if Money[i] != None:
            ans = max(ans,A[i] - Money[i])
    return ans

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]

    A = [None] + A
    print(solve(A,XY,N,M))

if __name__ == "__main__":
    main()