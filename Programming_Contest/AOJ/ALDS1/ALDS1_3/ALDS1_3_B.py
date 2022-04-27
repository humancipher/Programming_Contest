n, q = map(int, input().split())
P = []
for i in range(n):
    P.append(input().split())
for i in range(n):
    P[i][1]=int(P[i][1])

def RRSchedule(Que,q):
    n = len(Que)
    t = 0
    while len(Que) != 0:
        if Que[0][1] > q:
            t += q
            Que[0][1] -= q
            Que.append(Que[0])
            del Que[0]
        else:
            t += Que[0][1]
            print(Que[0][0], end=" ")
            print(t)
            del Que[0]

RRSchedule(P,q)
