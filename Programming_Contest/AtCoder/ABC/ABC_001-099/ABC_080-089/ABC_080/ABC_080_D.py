from sys import stdin
from itertools import accumulate
input = stdin.readline
INF = 10**10

def main():
    n,wlimit = map(int,input().split())
    wmin = INF
    WV = list()
    for _ in range(n):
        w,v = map(int,input().split())
        wmin = min(wmin,w)
        WV.append((w,v))
    V4 = [[] for _ in range(4)]
    for w,v in WV:
        V4[w-wmin].append(v)
    for i in range(4):
        V4[i].append(0)
        V4[i].sort(reverse=True)
        V4[i] = [0] + V4[i]
        V4[i] = list(accumulate(V4[i]))
    ans = 0
    for a in range(len(V4[0])):
        for b in range(len(V4[1])):
            for c in range(len(V4[2])):
                for d in range(len(V4[3])):
                    if a*wmin + b*(wmin+1) + c*(wmin+2) + d*(wmin+3) <= wlimit:
                        ans = max(ans,V4[0][a] + V4[1][b] + V4[2][c] + V4[3][d])
                    else:
                        break
                if a*wmin + b*(wmin+1) + c*(wmin+2) > wlimit:
                    break
            if a*wmin + b*(wmin+1) > wlimit:
                break
        if a*wmin > wlimit:
            break
    print(ans)

if __name__ == "__main__":
    main()
