x = int(input())

n = 1
while True:
    if n*(n+1)//2 < x:
        n += 1
    else:
        break
print(n)
