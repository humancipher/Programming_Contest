from heapq import heapify,heappop,heappush

def solve(AB,M):
    Shift = [[] for _ in range(M+1)] #Shift[i]:ちょうどi日目までなら間に合う
    for a,b in AB:
        if M >= a:
            Shift[M-a].append(b)
    for i in range(M):
        Shift[i].sort(reverse=True)
    Work = [] #実際に仕事して得る報酬のリスト
    heapify(Work)
    for i in range(M):
        pt = 0
        while len(Work) < i+1 and pt < len(Shift[i]):
            heappush(Work,Shift[i][pt])
            pt += 1
            if len(Work) == i+1:
                while pt < len(Shift[i]):
                    small = heappop(Work)
                    if small < Shift[i][pt]:
                        heappush(Work,Shift[i][pt])
                        pt += 1
                    else:
                        heappush(Work,small)
                        break
    return sum(Work)

def main():
    N,M = map(int,input().split())
    AB = list(map(int,input().split()) for _ in range(N))
    print(solve(AB,M))

if __name__ == "__main__":
    main()
