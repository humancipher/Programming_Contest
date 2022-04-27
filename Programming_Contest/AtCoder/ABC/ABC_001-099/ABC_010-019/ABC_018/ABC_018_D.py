def hw(x):
    cnt = 0
    while x > 0:
        if x % 2 != 0:
            cnt += 1
        x //= 2
    return cnt

def main():
    n,m,p,q,r = map(int,input().split())
    G = [list() for _ in range(n)]
    for _ in range(r):
        x,y,z = map(int,input().split())
        G[x-1].append((y-1,z))

    ans = 0
    for b in range(2**m):
        if hw(b) <= q:
            Tmp = [0] * n
            for i in range(n):
                for y,z in G[i]:
                    if b & 2**y != 0:
                        Tmp[i] += z
            Tmp.sort(reverse=True)
            ans = max(ans,sum(Tmp[:p]))
    print(ans)

if __name__ == "__main__":
    main()
