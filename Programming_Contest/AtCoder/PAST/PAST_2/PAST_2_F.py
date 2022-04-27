from heapq import heappop,heappush

def work(AB,N):
    Task = [[] for _ in range(N+1)]
    #Task[i]:i日目で実行可能なタスクでのポイント
    for i in range(N):
        a,b = AB[i][0],AB[i][1]
        Task[a].append(-b)

    OP,Task_ac = [],[]
    for i in range(1,N+1):
        for t in Task[i]:
            heappush(Task_ac,t)
        OP.append(-heappop(Task_ac))

    for i in range(1,N):
        OP[i] += OP[i-1]

    return OP

def main():
    N = int(input())
    AB = [list(map(int,input().split())) for _ in range(N)]

    ans = work(AB,N)
    for i in range(N):
        print(ans[i])

if __name__ == "__main__":
    main()
