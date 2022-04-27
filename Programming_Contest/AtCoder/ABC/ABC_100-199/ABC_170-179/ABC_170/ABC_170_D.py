def solve(A,N):
    A.sort()
    if N == 1:
        return 1
    elif N == 2:
        if A[1] == A[0]:
            return 0
        elif A[1] % A[0] == 0:
            return 1
        else:
            return 2
    elif A[0] == 1:
        if A[1] >= 2:
            return 1
        else:
            return 0
    else:
        Col = set()
        if A[0] == A[1]:
            Col.add(A[0])
        for i in range(1,N-1):
            if A[i-1] == A[i] or A[i] == A[i+1]:
                Col.add(A[i])
        if A[N-1] == A[N-2]:
            Col.add(A[N-1])

        Mul = set()
        cand = set()
        for i in range(N):
            if A[i] not in Mul:
                if A[i] not in Col:
                    cand.add(A[i])
                for d in range(1,(A[N-1]//A[i])+1):
                    Mul.add(A[i] * d)

        return len(cand)

def main():
    N = int(input())
    A = list(map(int,input().split()))

    print(solve(A,N))

if __name__ == "__main__":
    main()
