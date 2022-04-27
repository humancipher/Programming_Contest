T = int(input())
N,member = [],[]
for i in range(T):
    N.append(int(input()))
    member.append(list(map(int,input().split())))
    member[-1].sort()

for i in range(T):
    min_diff = 2000
    for j in range(1,N[i]):
        min_diff = min(member[i][j]-member[i][j-1],min_diff)
    print(min_diff)
