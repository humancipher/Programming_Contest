def mex(A,M): #mex(A[:M])
    D = dict()
    for a in A:
        if a in D:
            D[a] += 1
        else:
            D[a] = 1
    a = 0
    while True:
        if a not in D:
            return (D,a)
        else:
            a += 1

def mex_fix(D,kesu,ireru,ans): #辞書,消すやつ、入れるやつ、暫定解
    if D[kesu] == 1:
        D.pop(kesu)
    else:
        D[kesu] -= 1
    if ireru not in D:
        D[ireru] = 1
    else:
        D[ireru] += 1

    if kesu not in D:
        ans = kesu
        return (D,ans)
    elif ireru != ans:
        return (D,ans)
    else:
        while True:
            ans += 1
            if ans not in D:
                return (D,ans)

def solve(A,M,N):
    mx = mex(A[:M],M)
    D,ans = mx[0],mx[1]
    for i in range(N-M):
        tmp = mex_fix(D,A[i],A[i+M],ans)
        D,ans = tmp[0],min(ans,tmp[1])
    return ans

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    print(solve(A,M,N))

if __name__ == "__main__":
    main()
