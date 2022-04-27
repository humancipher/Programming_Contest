a,b,c,d = map(int,input().split())

r,cnt = 0,0
while cnt < 10**7:
    if a <= r * d:
        break
    else:
        a += b
        r += c
        cnt += 1
if cnt == 10**7:
    print(-1)
else:
    print(cnt)
