T = [int(input()) for _ in range(5)]
U = [T[i] for i in range(5)]

for i in range(5):
    if T[i] % 10 == 0:
        T[i] = 10
    else:
        T[i] %= 10
    U[i] += (10-T[i])

ans = sum(U)

T.sort()
ans -= (10-T[0])

print(ans)
