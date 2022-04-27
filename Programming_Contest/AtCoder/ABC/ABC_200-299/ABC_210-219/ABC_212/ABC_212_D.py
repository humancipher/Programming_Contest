from heapq import heapify,heappop,heappush

Ans = list()
q = int(input())
    
plus = 0
Ball = list()
heapify(Ball)

for _ in range(q):
    Que = list(map(int,input().split()))
    if Que[0] == 1:
        heappush(Ball,Que[1]-plus)
    if Que[0] == 2:
        plus += Que[1]
    if Que[0] == 3:
        Ans.append(heappop(Ball)+plus)
for i in range(len(Ans)):
    print(Ans[i])