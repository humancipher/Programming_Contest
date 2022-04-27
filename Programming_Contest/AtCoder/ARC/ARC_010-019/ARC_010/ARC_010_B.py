n = int(input())
HD = [tuple(map(int,input().split("/"))) for _ in range(n)]

M = [0,31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(1,13):
    M[i] += M[i-1]

D = [False for _ in range(367)] #D[i]:i日目が休日
for i in range(1,367):
    if i % 7 == 1 or i % 7 == 0:
        D[i] = True

for h,d in HD:
    if not D[M[h-1]+ d]:
        D[M[h-1]+d] = True
    else:
        day = M[h-1]+d+1
        while day <= 366:
            if not D[day]:
                D[day] = True
                break
            else:
                day += 1

ans,cnt = 0,0
for i in range(1,367):
    if D[i]:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0
ans = max(ans,cnt)
print(ans)
