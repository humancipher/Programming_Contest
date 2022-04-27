def possible(W,n,p,K):
    k,s = 1,0
    for i in range(n):
        if s + W[i] <= p:
            s += W[i]
        else:
            if W[i] <= p:
                s = W[i]
                k += 1
                if k > K:
                    return False
            else:
                return False
    return True

def solve(W,n,K):
    l,r = 0,sum(W)
    while r - l > 1:
        mid = (l+r)//2
        if possible(W,n,mid,K):
            r = mid
        else:
            l = mid
    return r

def main():
    n,k = map(int,input().split())
    W = [int(input()) for _ in range(n)]
    print(solve(W,n,k))

if __name__ == "__main__":
    main()
