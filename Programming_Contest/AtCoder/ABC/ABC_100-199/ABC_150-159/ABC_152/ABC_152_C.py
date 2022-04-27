N = int(input())
P = list(map(int,input().split()))

count,min = 0,P[0]
for i in range(N):
    if min >= P[i]:
        count += 1
        min = P[i]
print(count)
