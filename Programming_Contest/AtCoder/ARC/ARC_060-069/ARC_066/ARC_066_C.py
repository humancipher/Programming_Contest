def solve(A,N,M):
    #正しく並べると
    #Nが奇数: N-1 N-3 .... 2 0 2 .... N-3 N-1
    #Nが偶数: N-1 N-3 ... 3 1 1 3 ... N-3 N-1
    #になるはず

    A.sort(reverse = True)

    if N % 2 != 0:
        if A[len(A)-1] == 0:
            A.pop()
        else:
            return 0

    ans = pow(2,len(A)//2,M)
    a = 1
    if N % 2 != 0:
        a += 1
    while len(A) > 0:
        if A[len(A)-1] == a and A[len(A)-2] == a:
            A.pop()
            A.pop()
            a += 2
        else:
            return 0
    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))
    M = 10**9 + 7

    print(solve(A,N,M))

if __name__ == "__main__":
    main()
