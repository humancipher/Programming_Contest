a,b,c = map(int,input().split())
ans = -1
for x in range(a,b+1):
    if x% c == 0:
        ans = x
        break
print(ans)
