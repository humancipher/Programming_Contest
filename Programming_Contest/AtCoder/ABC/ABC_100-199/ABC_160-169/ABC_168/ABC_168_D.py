from queue import Queue

def bfs(AB,N):
    S = [None for _ in range(N+1)]
    #S[i]:部屋iにつけるべきサイン
    AB_N = [set() for _ in range(N+1)]
    for ab in AB:
        a,b = ab[0],ab[1]
        AB_N[a].add((a,b))

    q = Queue()
    q.put(1)

    while not q.empty():
        p = q.get()
        for ab in AB_N[p]:
            a,b = ab[0],ab[1]
            if a == p:
                if  S[b] == None:
                    q.put(b)
                    S[b] = p

    can = True
    for i in range(2,N+1):
        if S[i] == None:
            can = False

    if can:
        return S[2:]
    else:
        return -1

def main():
    N,M = map(int,input().split())
    AB = [tuple(map(int,input().split())) for _ in range(M)]

    AB_ = set(AB)
    for i in range(M):
        AB_.add((AB[i][1],AB[i][0]))
    AB = AB_

    ans = bfs(AB,N)
    if ans == -1:
        print("No")
    else:
        print("Yes")
        for i in range(len(ans)):
            print(ans[i])

if __name__ == "__main__":
    main()
