def rewrite(S,N):
    for i in reversed(range(N-1)):
        for j in range(1,2*N-2):
            if (S[i+1][j-1] == "X" \
            or S[i+1][j] == "X" \
            or S[i+1][j+1] == "X") \
            and S[i][j] == "#":
                S[i][j] = "X"

    return S

def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]

    S = rewrite(S,N)
    for i in range(N):
        S[i] = "".join(S[i])
        print(S[i])

if __name__ == "__main__":
    main()
