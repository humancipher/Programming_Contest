def study(A,C,m,n,b,x):
    B = [0 for _ in range(m)]
    cost = 0
    for i in range(n):
        if b[i] == "1":
            for j in range(m):
                B[j] += A[i][j]
            cost += C[i]
    if min(B) >= x:
        return (True,cost)
    else:
        return (False,-1)

def pad(b,n):
    if len(b) < n:
        b = "0"*(n-len(b)) + b
    return b

def main():
    N,M,X = map(int,input().split())
    CA = [list(map(int,input().split())) for _ in range(N)]

    C = [CA[i][0] for i in range(N)]
    A = [CA[i][1:] for i in range(N)]

    INF = 12*10**5+1
    ans = INF
    for i in range(2**N):
        b = pad(bin(i)[2:],N)
        st = study(A,C,M,N,b,X)
        if st[0]:
            cost = st[1]
            ans = min(ans,cost)

    if ans < INF:
        print(ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()
