INF = 10**9

def judge(XC,t): #時間tでまとめられるかどうか
    minus,plus = -INF,INF
    for x,c in XC:
        minus = max(minus,x - t/c)
        plus = min(plus,x + t/c)
    return plus >= minus

def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    XC,YC = [],[]
    for _ in range(n):
        x,y,c = map(int,input().split())
        XC.append((x,c))
        YC.append((y,c))
    left,right = 0,INF
    while right - left > 10**(-5):
        mid = (right+left) / 2
        if judge(XC,mid) and judge(YC,mid):
            right = mid
        else:
            left = mid
    print(left)

if __name__ == "__main__":
    main()
