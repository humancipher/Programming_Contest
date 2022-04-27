from sys import setrecursionlimit

setrecursionlimit(10**6)

def dfs(T,n,st,Ans,Visited):
    Ans.append(st)
    Visited[st] = True
    for nxt in T[st]:
        if not Visited[nxt]:
            dfs(T,n,nxt,Ans,Visited)
            Ans.append(st)

def main():
    n = int(input())
    T = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        T[a].append(b)
        T[b].append(a)
    for i in range(1,n+1):
        T[i].sort()
    Ans = []
    Visited = [False] * (n+1)
    dfs(T,n,1,Ans,Visited)
    print(" ".join(map(str,Ans)))

if __name__ == "__main__":
    main()
