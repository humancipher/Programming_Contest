N,T = map(int,input().split())
ABC = []
sumA,sumB = 0,0
for _ in range(N):
    a,b = map(int,input().split())
    c = a-b
    ABC.append([a,b,c])
    sumA += a
    sumB += b

if sumB > T:
    print(-1)
else:
    ABC.sort(key = lambda x:x[2],reverse=True)
    ABC.append([0,0,0])
    for i in range(N+1):
        if sumA <= T:
            print(i)
            break
        else:
            sumA -= ABC[i][2]
