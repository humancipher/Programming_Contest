T = int(input())
ab = [list(map(int,input().split())) for _ in range(T)]

for i in range(T):
    a,b = ab[i][0],ab[i][1]
    print(max(min(a,b)*2,max(a,b))**2)
