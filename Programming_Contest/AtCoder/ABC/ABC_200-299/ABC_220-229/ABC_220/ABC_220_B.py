k = int(input())
a,b = input().split()

A,B = 0,0
for i in range(len(a)):
    A += int(a[i]) * k**(len(a)-i-1)
for i in range(len(b)):
    B += int(b[i]) * k**(len(b)-i-1)

print(A*B)