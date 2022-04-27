B,C = map(int,input().split())
s = -B - (C-1)//2
t = -B + (C-1)//2
u =  B - C//2
v = B + (C-2)//2

if C == 1:
    if B == 0:
        ans = 1
    else:
        ans = 2
else:
    if B > 0:
        if t < u:
            ans = (t-s+1) + (v-u+1)
        else:
            ans = v-s+1
    elif B < 0:
        if s > v:
            ans = (t-s+1) + (v-u+1)
        else:
            ans = t-u+1
    else:
        x = -C//2
        y = (C-1)//2
        ans = y-x+1
print(ans)
