def solve(A,N,K):
    for k in range(K):
        C = [0 for _ in range(N+1)]
        #C[i]:i番目の電球を照らす電球の数
        for i in range(N):
            C[max(i-A[i],0)] += 1
            C[min(i+A[i]+1,N)] -= 1
        for i in range(1,N):
            C[i] += C[i-1]

        if C[0] == N or C[N-1] == N:
            for i in range(N):
                A[i] = N
            break
        else:
            for i in range(N):
                A[i] = C[i]
    return A

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    ans = solve(A,N,K)

    print(" ".join(map(str,ans)))

if __name__ == "__main__":
    main()
