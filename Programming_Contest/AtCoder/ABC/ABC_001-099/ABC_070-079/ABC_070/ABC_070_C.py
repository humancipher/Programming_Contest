def gcd(a,b):
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    else:
        return gcd(b,a % b)

def lcm(a,b):
    return a * b // gcd(a,b)

def LCM(A):
    if len(A) == 1:
        return A[0]
    else:
        l = A[0]
        for i in range(1,len(A)):
            l = lcm(l,A[i])
        return l

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]

    print(LCM(T))

if __name__ == "__main__":
    main()
