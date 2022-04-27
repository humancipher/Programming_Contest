from queue import Queue

def solve(S,N):
    Next = dict() # Next(a)=set(aと隣接するドミノの文字)
    Vec = [(0,1),(0,-1),(1,0),(-1,0)]

    for i in range(2):
        for j in range(N):
            Next[S[i][j]] = set()

    for i in range(2):
        for j in range(N):
            for v in Vec:
                if 0 <= i + v[0] and i + v[0] < 2 \
                and 0 <= j + v[1] and j + v[1] < N:
                    Next[S[i][j]].add(S[i+v[0]][j+v[1]])
    
    Q = Queue()
    Q.put(S[0][0])
    Visited = set()
    ans = 1
    mod = 1000000007
    while not Q.empty():
        p = Q.get()
        if p not in Visited:
            ans *= max(3 - len(Next[p] & Visited),0)
            ans %= mod
            Visited.add(p)
            for nx in Next[p]:
                if nx not in Visited:
                    Q.put(nx)

    return ans

def main():
    N = int(input())
    S = [input() for _ in range(2)]

    print(solve(S,N))

if __name__ == "__main__":
    main()
