from math import factorial

N = 10**6-1
A = [str(i) for i in range(10)]

S = ""
while len(A) > 0:
    pt = N // factorial(len(A)-1)
    N %= factorial(len(A)-1)
    S += A[pt]
    A.pop(pt)

print(S)
