x,y = map(int,input().split())

if abs(x) < abs(y):
    cnt = abs(y)-abs(x)
    if x*y == 0:
        if y < 0:
            cnt += 1
    elif x*y < 0:
        cnt += 1
    elif x < 0:
        cnt += 2
    print(cnt)
elif abs(x) > abs(y):
    cnt = abs(x)-abs(y)
    if x*y == 0:
        if x > 0:
            cnt += 1
    elif x*y < 0:
        cnt += 1
    elif x > 0:
        cnt += 2
    print(cnt)
else:
    print(1)
