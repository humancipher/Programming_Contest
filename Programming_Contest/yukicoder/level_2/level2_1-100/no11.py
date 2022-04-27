w = int(input())
h = int(input())
n = int(input())
SK = set([tuple(map(int,input().split())) for _ in range(n)])

Mark = [0 for _ in range(w+1)]
Num = [0 for _ in range(h+1)]

for s,k in SK:
    Mark[s] += 1
    Num[k] += 1

ans = 0
for i in range(w+1):
    if Mark[i] > 0:
        ans += (h-Mark[i])
for i in range(h+1):
    if Num[i] > 0:
        ans += (w-Num[i])

col = 0
Counted = set()
for s0,k0 in SK:
    for s1,k1 in SK:
        if s0 != s1 and k0 != k1:
            if (s0,k1) not in SK:
                if (s0,k1) not in Counted:
                    col += 1
                    Counted.add((s0,k1))
            if (s1,k0) not in SK:
                if (s1,k0) not in Counted:
                    col += 1
                    Counted.add((s1,k0))
ans -= col
print(ans)
