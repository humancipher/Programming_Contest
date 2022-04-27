N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]

AB.sort(key = lambda x:x[0])

pt,money = 0,0
while M > 0 and pt < N:
    if M > AB[pt][1]:
        money += AB[pt][0] * AB[pt][1]
        M -= AB[pt][1]
    else:
        money += AB[pt][0] * M
        M = 0
    pt += 1

print(money)
