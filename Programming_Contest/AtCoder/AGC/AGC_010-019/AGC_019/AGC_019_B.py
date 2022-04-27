INF = 10**15

def judge(A,st,go):
    for a in A:
        st -= st % a
    return st >= go

def main():
    import sys
    input = sys.stdin.readline
    k = int(input())
    A = list(map(int,input().split()))
    left,right = 0,INF
    while right-left > 1:
        mid = (left+right)//2
        if judge(A,mid,2):
            right = mid
        else:
            left = mid
    ans1 = right
    left,right = 0,INF
    while right-left > 1:
        mid = (left+right)//2
        if judge(A,mid,3):
            right = mid
        else:
            left = mid
    ans2 = right
    if ans1 <= ans2-1:
        print(ans1,ans2-1)
    else:
        print(-1)

if __name__ == "__main__":
    main()
