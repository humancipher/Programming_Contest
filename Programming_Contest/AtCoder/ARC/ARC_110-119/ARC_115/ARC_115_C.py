def solve(N):
    A = [2 for _ in range(N+1)]
    A[1] = 1
    i = 2
    for i in range(2,N+1):
        for j in range(2,N//i+1):
            if A[i*j] == A[i]:
                A[i*j] += 1
    return " ".join(map(str,A[1:]))

def main():
    N = int(input())
    print(solve(N))

if __name__ == "__main__":
    main()
