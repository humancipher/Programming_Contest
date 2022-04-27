def inversion(A,N,K,M):
    B = [0 for _ in range(N)]
    C = [0 for _ in range(N)]
    #B[i]:i<j且つA[i]>A[j]を満たすjの個数
    #C[i]:A[i]<A[j]を満たすjの個数
    for i in range(N):
        for j in range(i+1,N):
            if A[i] > A[j]:
                B[i] += 1

    for i in range(N):
        for j in range(N):
            if A[i] > A[j]:
                C[i] += 1

    output = sum(B) * K
    output += sum(C) * K * (K-1) //2
    output %= M

    return output

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    M = 10**9+7

    print(inversion(A,N,K,M))

if __name__ == "__main__":
    main()
