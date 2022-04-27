n = int(input())

def fib(n):
    Fib = [1,1]
    if n == 0 or n == 1:
        return Fib[n]
    for i in range(2,n+1):
        Fib.append(Fib[i-1] + Fib[i-2])
    return Fib[n]

print(fib(n))
