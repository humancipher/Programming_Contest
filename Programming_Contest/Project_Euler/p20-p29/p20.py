from math import factorial

N = 100
fact = str(factorial(N))
ans = 0
for i in range(len(fact)):
    ans += int(fact[i])
print(ans)
