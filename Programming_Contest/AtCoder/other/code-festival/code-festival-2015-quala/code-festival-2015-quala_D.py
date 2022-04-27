def judge(X,n,m,t):
    bef = 0
    for i in range(m):
        if X[i] - t > bef+1:
            return False
        else:
            if bef+1 >= X[i]:
                bef = X[i]+t
            else:
                migi = (t-(X[i]-bef-1))//2
                #先に右に行くパターンjと左に行くパターンのいい方を選択する
                bef = max(X[i]+t-2*(X[i]-bef-1),X[i]+migi)
    return bef >= n

def solve(X,n,m):
    left,right = -1,2*n
    while right - left > 1:
        mid = (left+right)//2
        if judge(X,n,m,mid):
            right = mid
        else:
            left = mid
    return right

def main():
    n,m = map(int,input().split())
    X = [int(input()) for _ in range(m)]
    print(solve(X,n,m))

if __name__ == "__main__":
    main()
