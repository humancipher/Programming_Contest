N = int(input())
A = list(map(int,input().split()))

Count = dict()
for a in A:
    for c in range(-1,2):
        if a + c not in Count:
            Count[a+c] = 1
        else:
            Count[a+c] += 1

ans = 0
for c in Count:
    ans = max(ans,Count[c])

print(ans)
