from copy import deepcopy

def tournament(A,N):
    count = 1
    OP = [1 for _ in range(2**N)]

    while count < N:
        B = []
        for i in range(len(A)//2):
            if A[2*i][1] > A[2*i+1][1]:
                B.append([A[2*i][0],A[2*i][1]])
            else:
                B.append([A[2*i+1][0],A[2*i+1][1]])
            OP[B[len(B)-1][0]] += 1
        A = deepcopy(B)
        count += 1

    return OP

def main():
    N = int(input())
    A = list(map(int,input().split()))
    for i in range(2**N):
        A[i] = [i,A[i]]

    ans = tournament(A,N)
    for i in range(2**N):
        print(ans[i])

if __name__ == "__main__":
    main()
