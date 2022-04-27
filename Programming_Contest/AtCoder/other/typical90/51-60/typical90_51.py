from bisect import bisect_right
from sys import stdin
input = stdin.readline

def half_pat(AH,nh):
    R = [[] for _ in range(nh+1)] #R[i]:i個選んで得られるパターン
    for i in range(2**nh):
        hw,s = 0,0
        for j in range(nh):
            if i & 1<<j:
                hw += 1
                s += AH[j]
        R[hw].append(s)
    for i in range(nh+1):
        R[i].sort()
    return R

def main():
    n,k,p = map(int,input().split())
    A = list(map(int,input().split()))
    A1,A2 = A[:n//2],A[n//2:]
    R1,R2 = half_pat(A1,len(A1)),half_pat(A2,len(A2))
    ans = 0
    for i in range(len(R1)):
        for j in range(len(R1[i])):
            if 0 <= k-i and k-i < len(R2):
                ans += bisect_right(R2[k-i],p-R1[i][j])
    print(ans)

if __name__ == "__main__":
    main()