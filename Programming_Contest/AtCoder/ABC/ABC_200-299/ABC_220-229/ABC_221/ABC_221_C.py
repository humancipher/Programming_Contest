N = list(input())
for i in range(len(N)):
    N[i] = int(N[i])
N.sort()
a,b = 0,0
for i in range(len(N)):
    if a <= b:
        a = 10 * a + N.pop()
    else:
        b = 10 * b + N.pop()
print(a*b)