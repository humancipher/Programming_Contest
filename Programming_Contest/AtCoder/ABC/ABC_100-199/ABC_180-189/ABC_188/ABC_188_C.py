def solve(A):
    if len(A) == 2:
        if A[0][0] < A[1][0]:
            return A[0][1]
        else:
            return A[1][1]
    else:
        B = []
        for i in range(0,len(A),2):
            if A[i][0] < A[i+1][0]:
                B.append(A[i+1])
            else:
                B.append(A[i])
        return solve(B)

def main():
    N = int(input())
    A = list(map(int,input().split()))

    B = [[A[i],i+1] for i in range(2**N)]
    print(solve(B))

if __name__ == "__main__":
    main()
