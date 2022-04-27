n = int(input())
A = list(map(int,input().split()))
Cut = [0,360]
now = 0
for i in range(n):
    now += A[i]
    now %= 360
    Cut.append(now)
Cut.sort()
ans = 0
for i in range(len(Cut)-1):
    ans = max(ans,Cut[i+1]-Cut[i])
print(ans)