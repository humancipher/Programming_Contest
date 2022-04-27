def nsin(x,n): #xをn進法を見たときの値
    x = str(x)
    ans = 0
    for i in range(len(x)):
        ans += int(x[i]) * n**(len(x)-i-1)
    return ans

def maxX(x):
    x = str(x)
    ans = 0
    for i in range(len(x)):
        ans = max(ans,int(x[i]))
    return ans

def solve(X,M):
    if len(str(X)) >= 2:
        mx = maxX(X)
        left,right = mx,M+1
        while left < right - 1:
            mid = (left+right)//2
            if nsin(X,mid) <= M:
                left = mid
            else:
                right = mid
        ans = left - mx
    else:
        if X <= M:
            ans = 1
        else:
            ans = 0
    return ans

def main():
    X = int(input())
    M = int(input())
    print(solve(X,M))

if __name__ == "__main__":
    main()

