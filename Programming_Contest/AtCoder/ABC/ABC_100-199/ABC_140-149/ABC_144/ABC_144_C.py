import math

N = int(input())
sq = int(math.sqrt(N))

if N == 2 or N == 3:
    print(N-1)
elif sq*sq == N:
    print(2*sq-2)
else:
    for i in reversed(range(1,sq+1)):
        if N % i == 0:
            print(i+(N//i)-2)
            break
