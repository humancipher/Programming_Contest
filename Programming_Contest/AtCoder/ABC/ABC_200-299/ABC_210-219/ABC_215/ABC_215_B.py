n = int(input())
p,k = 1,0
while True:
    p *= 2
    if p <= n:
        k += 1
    else:
        break
print(k)
