from bisect import bisect_left
INF = 10**15

def solve(H,W,N):
    H.sort()
    L,R = [0],[]
    ans = INF
    for i in range(N-1):
        if i % 2 == 0:
            L.append(H[i+1]-H[i])
        else:
            R.append(H[i+1]-H[i])
    R.append(0)
    for i in range(len(R)//2):
        R[i],R[len(R)-1-i] = R[len(R)-1-i],R[i]
    for i in range(len(L)-1):
        L[i+1] += L[i]
        R[i+1] += R[i]
    for w in W:
        x = bisect_left(H,w)
        if x % 2 == 1:
            tmp = abs(w-H[x-1]) + L[(x-1)//2] + R[(N-x)//2]
        else:
            tmp = abs(w-H[x]) + L[x//2] + R[(N-x-1)//2]
        ans = min(ans,tmp)
    return ans

def main():
    NM = list(map(int,input().split()))
    N = NM[0]
    H = list(map(int,input().split()))
    W = list(map(int,input().split()))
    print(solve(H,W,N))

if __name__ == "__main__":
    main()
