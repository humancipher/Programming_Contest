def solve(S,N):
    E,W = [0 for _ in range(N)],[0 for _ in range(N)]
    for i in range(N):
        if S[i] == "E":
            E[i] = 1
        else:
            W[i] = 1

    for i in range(1,N):
        E[i] += E[i-1]
        W[i] += W[i-1]

    ans = N
    for i in range(1,N):
        ans = min(ans,W[i-1]+(E[N-1]-E[i]))
    ans = min(ans,E[N-1]-E[0])

    return ans

def main():
    N = int(input())
    S = input()

    print(solve(S,N))

if __name__ == "__main__":
    main()
