#pypyなら間に合う

def prefix(A,N):
    pref = [[0 for _ in range(N)] for _ in range(N)]
    #pref[i][j]:区間iからjでの埋蔵量
    for i in range(N):
        pref[i][i] = A[i]

    for i in range(N):
        for j in range(1,N):
            pref[i][j] += pref[i][j-1]
    for j in range(N):
        for i in reversed(range(1,N)):
            pref[i-1][j] += pref[i][j]

    return pref

def main():
    N = int(input())
    A = list(map(int,input().split()))

    pref = prefix(A,N)

    for k in range(1,N+1):
        ans = 0
        for i in range(N-k+1):
            ans = max(ans,pref[i][i+k-1])
        print(ans)

if __name__ == "__main__":
    main()
