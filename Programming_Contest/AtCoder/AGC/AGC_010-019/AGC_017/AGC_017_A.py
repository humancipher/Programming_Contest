from math import factorial

def comb(n,r):
    return factorial(n) // (factorial(n-r) * factorial(r))

def main():
    N,P = map(int,input().split())
    A = list(map(int,input().split()))

    even,odd = 0,0
    for i in range(N):
        if A[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    a,b = 0,0
    b = 2**even

    for i in range(odd+1):
        if i % 2 == P:
            a += comb(odd,i)

    print(a*b)

if __name__ == "__main__":
    main()
