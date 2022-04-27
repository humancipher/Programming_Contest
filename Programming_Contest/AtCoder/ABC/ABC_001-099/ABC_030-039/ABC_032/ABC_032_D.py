from bisect import bisect_right
import sys
input = sys.stdin.readline

def pat1(VW,n,w):
    HF = VW[:n//2]
    HF2 = VW[n//2:]
    D1,D2 = dict(),dict()
    DL1,DL2 = list(),list()
    DLB2 = list()
    for i in range(2**(len(HF))):
        a,b = 0,0
        for j in range(len(HF)):
            if 2**j & i:
                a += HF[j][0]
                b += HF[j][1]
        if b <= w:
            if b in D1:
                D1[b] = max(D1[b],a)
            else:
                D1[b] = a
    for i in range(2**(len(HF2))):
        a,b = 0,0
        for j in range(len(HF2)):
            if 2**j & i:
                a += HF2[j][0]
                b += HF2[j][1]
        if b <= w:
            if b in D2:
                D2[b] = max(D2[b],a)
            else:
                D2[b] = a
    for x in D1:
        DL1.append([x,D1[x]])
    for x in D2:
        DL2.append([x,D2[x]])
        DLB2.append(x)
    DL1.sort(key = lambda x:x[0])
    DL2.sort(key = lambda x:x[0])
    DLB2.sort()
    for i in range(len(DL1)-1):
        DL1[i+1][1] = max(DL1[i+1][1],DL1[i][1])
    for i in range(len(DL2)-1):
        DL2[i+1][1] = max(DL2[i+1][1],DL2[i][1])
    ans = 0
    for i in range(len(DL1)):
        bs = bisect_right(DLB2,w-DL1[i][0])
        tmp = DL1[i][1] + DL2[bs-1][1]
        ans = max(ans,tmp)
    return ans

def pat2(VW,n,w,sumW):
    dp = [0] * (sumW+1)
    for i in range(n):
        ndp = [0] * (sumW+1)
        for j in range(sumW+1):
            if j >= VW[i][1]:
                ndp[j] = max(dp[j],dp[j-VW[i][1]] + VW[i][0])
            else:
                ndp[j] = dp[j]
        dp = ndp
    if sumW >= w:
        return dp[w]
    else:
        return dp[-1]

def pat3(VW,n,w,sumV):
    INF = 10**12
    dp = [INF] * (sumV+1) #dp[j]:価値jを実現する最小重量
    dp[0] = 0
    for i in range(n):
        ndp = [INF] * (sumV+1)
        for j in range(sumV+1):
            if j >= VW[i][0]:
                ndp[j] = min(dp[j],dp[j-VW[i][0]] + VW[i][1])
            else:
                ndp[j] = dp[j]
        dp = ndp
    ans = 0
    for i in reversed(range(len(dp))):
        if dp[i] <= w:
            ans = i
            break
    return ans

def main():
    n,w = map(int,input().split())
    sumV,sumW = 0,0
    maxV,maxW = 0,0
    VW = list()
    for _ in range(n):
        a,b = map(int,input().split())
        VW.append([a,b])
        sumV += a
        sumW += b
        maxV = max(maxV,a)
        maxW = max(maxW,b)
    if n <= 30:
        print(pat1(VW,n,w))
    elif maxW <= 1000:
        print(pat2(VW,n,w,sumW))
    else:
        print(pat3(VW,n,w,sumV))

if __name__ == "__main__":
    main()
