X,Y = map(int,input().split())

money = [3*10**5,2*10**5,10**5]

ans = 0
if X == 1 and Y == 1:
    ans = 2*money[0] + 4*10**5
    print(ans)
else:
    if X <= 3:
        ans += money[X-1]
    if Y <= 3:
        ans += money[Y-1]
    print(ans)
