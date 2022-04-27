N,A,B = map(int,input().split())

q = N // (A+B)
r = N % (A+B)
if r <= A:
    print(q*A+r)
else:
    print(q*A+A)
