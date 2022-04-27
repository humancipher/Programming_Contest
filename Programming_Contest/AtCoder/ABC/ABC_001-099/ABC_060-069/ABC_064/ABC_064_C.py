N = int(input())
a = list(map(int,input().split()))

C = [0 for _ in range(9)]

for i in range(N):
    if a[i] // 400 < 8:
        C[a[i]//400] = 1
    else:
        C[8] += 1

ans_min = max(1,sum(C[:8]))
ans_max = sum(C)
print(ans_min,ans_max)
