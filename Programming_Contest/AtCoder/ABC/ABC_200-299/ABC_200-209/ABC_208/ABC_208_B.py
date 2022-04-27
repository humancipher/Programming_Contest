p = int(input())
C = [1]
for i in range(9):
    C.append(C[-1] * (i+2))
ans = 0
for i in reversed(range(10)):
    d = p//C[i]
    ans += d
    p -= d * C[i]
print(ans)