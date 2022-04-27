from queue import Queue

def solve(AB,N):
    E_next = [set() for _ in range(N+1)] #E_next[i]:頂点iに直接つながる頂点の集合
    Used = [set() for _ in range(N+1)] #Used[i]:頂点iをつなげる辺で用いら色の集合
    root = 1 #頂点1を根とする根付き木で考える
    C = dict() #C[(a,b)]: 辺(a,b)の色
    for a,b in AB:
        E_next[a].add(b)
        E_next[b].add(a)
    
    Q = Queue()
    Q.put(root)
    while not Q.empty():
        q = Q.get()
        color = 1
        for c in E_next[q]:
            if (q,c) not in C:
                while True:
                    if color not in Used[q]:
                        C[(q,c)] = color
                        C[(c,q)] = color
                        Used[q].add(color)
                        Used[c].add(color)
                        break
                    else:
                        color += 1
                Q.put(c)
    
    Ans = []
    for i in range(len(AB)):
        Ans.append(C[(AB[i][0],AB[i][1])])
    
    return Ans

def main():
    N = int(input())
    AB = [list(map(int,input().split())) for _ in range(N-1)]

    ans = solve(AB,N)
    print(max(ans))
    for i in range(len(ans)):
        print(ans[i])

if __name__ == "__main__":
    main()
