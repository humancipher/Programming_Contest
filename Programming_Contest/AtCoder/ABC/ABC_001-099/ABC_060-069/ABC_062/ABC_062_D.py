def main():
    from heapq import heapify,heappush,heappop
    import sys
    input = sys.stdin.readline
    n = int(input())
    A = tuple(map(int,input().split()))
    BL,BR = [],[]
    for i in range(n):
        BL.append(A[i])
        BR.append(-A[3*n-1-i]) #後半は最小化したい
    CL,CR = [],[]
    CL.append(sum(BL))
    CR.append(sum(BR))
    heapify(BL)
    heapify(BR)
    for i in range(n,2*n):
        bl = heappop(BL)
        br = heappop(BR)
        if bl < A[i]:
            CL.append(CL[-1]-bl+A[i])
            heappush(BL,A[i])
        else:
            CL.append(CL[-1])
            heappush(BL,bl)
        if -br > A[3*n-1-i]:
            CR.append(CR[-1]-br-A[3*n-1-i])
            heappush(BR,-A[3*n-1-i])
        else:
            CR.append(CR[-1])
            heappush(BR,br)
    ans = CL[0]+CR[n]
    for i in range(n+1):
        ans = max(ans,CL[i]+CR[n-i])
    print(ans)

if __name__ == "__main__":
    main()
