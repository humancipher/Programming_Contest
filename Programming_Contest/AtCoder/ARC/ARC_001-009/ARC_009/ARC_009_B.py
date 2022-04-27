def convert(dict,n):
    n = list(str(n))
    for i in range(len(n)):
        n[i] = str(dict[int(n[i])])
    n = "".join(n)
    n = int(n)
    return n

def main():
    enc = list(map(int,input().split()))
    N = int(input())
    a = [input() for _ in range(N)]

    dec = [None for _ in range(10)]
    for i in range(10):
        dec[enc[i]] = i

    for i in range(N):
        a[i] = convert(dec,a[i])
    a.sort()
    
    for i in range(N):
        a[i] = convert(enc,a[i])
        print(a[i])

if __name__ == "__main__":
    main()
