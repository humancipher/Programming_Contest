from math import sqrt

N = int(input())

def ans(n):
    a,b = 1,n
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            a,b = i,n//i
    return max(len(str(a)),len(str(b)))

print(ans(N))
