S = input()
N = int(input())
T = [input() for _ in range(N)]

for i in range(N):
    T[i] = T[i] + T[i]

ans = 0
for i in range(N):
    if T[i].find(S) != -1:
        ans += 1

print(ans)
