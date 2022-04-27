N,M = map(int,input().split())
A = list(map(int,input().split()))
BC = [list(map(int,input().split())) for _ in range(M)]

A.sort()
BC.sort(reverse=True,key = lambda x:x[1])

pt,card,index = 0,BC[0][1],0
while True:
    for i in range(BC[index][0]):
        if pt < N:
            #このときにA[pt]がout of rangeでないかどうかのチェックは毎回必要
            A[pt] = max(A[pt],card)
        else:
            break
        pt += 1

    index += 1
    if index < M:
        card = BC[index][1]
    else:
        break

print(sum(A))
