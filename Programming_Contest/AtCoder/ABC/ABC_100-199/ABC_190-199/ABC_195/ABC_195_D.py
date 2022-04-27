def b_search(A,key): #A[i] >= keyを満たす最小のi
    if A[0] < key:
        return -1
    else:
        left,right = 0,len(A)
        while right - left > 1:
            mid = (left+right)//2 #A[left] >= key > A[right]
            if A[mid] < key:
                right = mid
            else:
                left = mid
        return left

def solve(WV,N,X,L,R):
    Y = X[:L] + X[R+1:]
    Y.sort(reverse=True)
    ans = 0
    for i in range(N):
        w,v = WV[i][0],WV[i][1]
        if len(Y) > 0:
            bs = b_search(Y,w)
            if bs >= 0:
                ans += v
                Y = Y[:bs] + Y[bs+1:]
        else:
            break
    return ans

def main():
    NMQ = list(map(int,input().split()))
    N,Q = NMQ[0],NMQ[2]
    WV = [list(map(int,input().split())) for _ in range(N)]
    WV.sort(key = lambda x:x[1],reverse=True)
    X = list(map(int,input().split()))
    Que = [list(map(int,input().split())) for _ in range(Q)]
    for i in range(Q):
        print(solve(WV,N,X,Que[i][0]-1,Que[i][1]-1))

if __name__ == "__main__":
    main()
