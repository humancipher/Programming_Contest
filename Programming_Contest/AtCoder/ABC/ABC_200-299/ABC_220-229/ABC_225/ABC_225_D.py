from collections import deque

n,q = map(int,input().split())
Mae = [i for i in range(n+1)] #Mae[i]:i番目の電車の前の電車(Mae[i]==iなら前に電車なし)
Usiro = [i for i in range(n+1)]

Ans = []
for _ in range(q):
    Que = list(map(int,input().split()))
    if Que[0] == 1:
        Usiro[Que[1]] = Que[2]
        Mae[Que[2]] = Que[1]
    if Que[0] == 2:
        Usiro[Que[1]] = Que[1]
        Mae[Que[2]] = Que[2]
    if Que[0] == 3:
        Deq = deque([Que[1]])
        left,right = Que[1],Que[1]
        while Mae[left] != left:
            Deq.appendleft(Mae[left])
            left = Mae[left]
        while Usiro[right] != right:
            Deq.append(Usiro[right])
            right = Usiro[right]
        ans = []
        while len(Deq) > 0:
            tmp = Deq.popleft()
            ans.append(tmp)
        Ans.append(ans)

for i in range(len(Ans)):
    ans = str(len(Ans[i])) + " " + " ".join(map(str,Ans[i]))
    print(ans)
