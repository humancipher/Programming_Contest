from math import ceil, inf
INF = 10**10

def judge(H,a,b,x): #x回で殲滅できるかどうか
    cnt = 0
    for h in H:
        if h-x*b > 0:
            cnt += ceil((h-b*x)/(a-b)) #中心を狙う必要がある回数
    return cnt <= x

def solve(H,a,b):
    left,right = 0,INF
    while right-left > 1:
        mid = (left+right)//2
        if judge(H,a,b,mid):
            right = mid
        else:
            left = mid
    return right

def main():
    n,a,b = map(int,input().split())
    H = [int(input()) for _ in range(n)]
    print(solve(H,a,b))

if __name__ == "__main__":
    main()
