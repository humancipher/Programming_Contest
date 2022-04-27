N = int(input())

A,B = 3,5
flag = 0
for a in range(1,1000):
    for b in range(1,1000):
        if A + B == N:
            print(a,b)
            flag = 1
            break
        if A + B > N:
            break
        if A + B < N:
            B *= 5
    A *= 3
    B = 5
    if A + B > N:
        break

if not flag:
    print(-1)
