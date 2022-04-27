ans = "second"
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 2 != 0:
        ans = "first"
print(ans)