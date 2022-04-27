M,D = map(int,input().split())

ans = 0
for m in range(M+1):
    for d in range(10,D+1):
        d1,d2 = d // 10,d % 10
        if m == d1 * d2 and d1 >= 2 and d2 >= 2:
            ans += 1

print(ans)
