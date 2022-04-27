from sys import stdin
input = stdin.readline

def main():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    Loop = list()
    Loopset = set()
    x,cnt = 0,0
    stop = False
    while cnt < k and not stop:
        if x % n not in Loopset:
            Loop.append(x % n)
            Loopset.add(x % n)
            x += A[x % n]
            cnt += 1
        else:
            stop = True
    if cnt == k:
        ans = x
    else:
        base = -1
        for i in range(len(Loop)):
            if x % n == Loop[i]:
                base = i
                break
        k -= base
        ans = 0
        for i in range(base):
            ans += A[Loop[i]]
        sho,amari = 0,0
        for i in range(base,len(Loop)):
            sho += A[Loop[i]]
        ans += sho * (k // (len(Loop)-base))
        k %= (len(Loop)-base)
        for i in range(k):
            amari += A[Loop[base+i]]
        ans += amari
    print(ans)

if __name__ == "__main__":
    main()
