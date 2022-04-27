import math
N = int(input())

tax = 1.08
n = N // tax

if math.floor((n) * tax) == N:
    print(int(n))
else:
    while 1:
        if math.floor(n * tax) == N:
            print(int(n))
            break
        elif math.floor(n * tax) < N:
            n += 1
        elif math.floor(n * tax) > N:
            print(":(")
            break
