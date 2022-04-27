n = input()
N = [int(n[i]) % 3 for i in range(len(n))]

ans = len(n)
S = sum(N) % 3
for i in range(2**len(n)):
    tmp,cnt = S,0
    for j in range(len(n)):
        if 2**j & i:
            tmp -= N[j]
            tmp %= 3
            cnt += 1
    if tmp == 0:
        ans = min(ans,cnt)
if ans == len(n):
    print(-1)
else:
    print(ans)

