N = int(input())
ab = [list(map(int,input().split())) for _ in range(N)]

money = 0
for a,b in ab:
    money += a*b

print(int(money*1.05))
