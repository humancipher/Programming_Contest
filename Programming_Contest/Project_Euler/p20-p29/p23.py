from math import sqrt

N = 28123

def divisor_sum(n):
    output = 0
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            output += i
            output += (n // i)
    if int(sqrt(n))**2 == n:
        output -= int(sqrt(n))
    output -= n
    return output

def decomposable(A,n):
    for a in A:
        if n - a in A:
            return True
    return False

Ex_Num,Ex_Num_undec = set([]),set([])
#N以下の過剰数の集合,過剰数2つの和に分解できないN以下の整数の集合
for i in range(1,N+1):
    if divisor_sum(i) > i:
        Ex_Num.add(i)

for i in range(1,N+1):
    if not decomposable(Ex_Num,i):
        Ex_Num_undec.add(i)

ans = sum(Ex_Num_undec)
print(ans)
