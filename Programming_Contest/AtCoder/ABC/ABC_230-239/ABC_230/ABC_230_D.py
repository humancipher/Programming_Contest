from sys import stdin

def main():
    n,d = map(int,input().split())
    LR = [list(map(int,input().split())) for _ in range(n)]
    LR.sort(key = lambda x:x[1])
    print(solve(LR,n,d))

def solve(LR,n,d):
    cnt = 1
    ptx = LR[0][1] + d - 1
    pty = 0
    while pty < n:
        if LR[pty][0] <= ptx:
            pty += 1
            if pty == n:
                break
        else:
            cnt += 1
            ptx = LR[pty][1] + d - 1
    return cnt

if __name__ == "__main__":
    main()
