from bisect import bisect_left

def solve(A,B,X,Y,N,M):
    time,cnt = 0,0
    update = True
    while update:
        pt_A = bisect_left(A,time)
        if pt_A == N:
            update = False
            break
        time = A[pt_A] + X
        pt_B = bisect_left(B,time)
        if pt_B == M:
            update = False
            break
        time = B[pt_B] + Y
        cnt += 1
    return cnt

def main():
    N,M = map(int,input().split())
    X,Y = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    print(solve(a,b,X,Y,N,M))

if __name__ == "__main__":
    main()
