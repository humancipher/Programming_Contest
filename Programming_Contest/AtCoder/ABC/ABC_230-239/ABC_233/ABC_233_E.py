x = list(input())
n = len(x)
for i in range(n):
    x[i] = int(x[i])
for i in range(n-1):
    x[i+1] += x[i]
A = [0] * (n+1)
carry = 0
for i in reversed(range(n)):
    A[i+1] = (x[i] + carry) % 10
    carry = (x[i]+carry) // 10
A[0] = carry
pt = 0
while True:
    if A[pt] == 0:
        pt += 1
    else:
        break
ans = "".join(map(str,A[pt:]))
print(ans)