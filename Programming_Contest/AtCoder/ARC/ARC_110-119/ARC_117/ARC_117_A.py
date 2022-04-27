b,a = map(int,input().split())

A,B = [],[]
if a == b:
    for i in range(1,a+1):
        A.append(-i)
        B.append(i)
if a > b:
    for i in range(1,a+1):
        A.append(-i)
    for i in range(1,b+1):
        B.append(i)
    sumA,sumB = sum(A),sum(B)
    B[-1] = -(sumA+sumB) + B[-1]
if a < b:
    for i in range(1,a+1):
        A.append(-i)
    for i in range(1,b+1):
        B.append(i)
    sumA,sumB = sum(A),sum(B)
    A[-1] = -(sumA+sumB) + A[-1]
print(" ".join(map(str,A+B)))
