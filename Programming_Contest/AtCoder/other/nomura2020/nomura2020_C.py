def mk_tree(A,N):
    B = [None for _ in range(N+1)]
    B[0] = 1
    #B[i]:深さiの頂点の個数
    A_sum = [A[i] for i in range(N+1)]
    for i in reversed(range(N)):
        A_sum[i] += A_sum[i+1]

    for i in range(1,N+1):
        B[i] = min(2*(B[i-1]-A[i-1]),A_sum[i])

    if B[N] == A[N]:
        return sum(B)
    else:
        return -1

def main():
    N = int(input())
    A = list(map(int,input().split()))

    print(mk_tree(A,N))

if __name__ == "__main__":
    main()
