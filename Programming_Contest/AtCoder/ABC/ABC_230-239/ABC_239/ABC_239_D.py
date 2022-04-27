def eratos(n):
    A = [True] * (n+1)
    A[0],A[1] = False,False
    pt = 2
    P = set()
    while pt**2 <= n:
        if A[pt]:
            for j in range(2,n//pt + 1):
                A[pt*j] = False
        pt += 1
    for i in range(n+1):
        if A[i]:
            P.add(i)
    return P

def main():
    import sys
    input = sys.stdin.readline
    a,b,c,d = map(int,input().split())
    ans = "Aoki"
    for i in range(a,b+1):
        P = eratos(i+d)
        flag = True
        for j in range(c,d+1):
            if i+j in P:
                flag = False
                break
        if flag:
            ans = "Takahashi"
        if ans == "Takahashi":
            break
    print(ans)

if __name__ == "__main__":
    main()
