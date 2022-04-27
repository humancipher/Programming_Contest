x,y = map(int,input().split())
y -= x
d = y // 10
if y % 10 != 0:
    d += 1
d = max(0,d)
print(d)