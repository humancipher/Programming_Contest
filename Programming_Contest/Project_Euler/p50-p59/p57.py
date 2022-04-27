def cont_fra(n):
    a = [None for _ in range(n)]
    b = [None for _ in range(n)]
    c = [None for _ in range(n)]
    a[0],b[0],c[0] = 1,2,3
    #a[i],b[i],c[i]:sqrt(2)を連分数で表現したとき
    #sqrt(2) = 1+a[i]/b[i] = c[i]/b[i]とする
    for i in range(1,n):
        a[i] = b[i-1]
        b[i] = a[i-1]+2*b[i-1]
        c[i] = a[i]+b[i]

    cb = [(str(c[i]),str(b[i])) for i in range(n)]

    return cb

def main():
    n = 1000

    cb = cont_fra(n)

    ans = 0
    for i in range(n):
        c,b = cb[i][0],cb[i][1]
        if len(c) > len(b):
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
