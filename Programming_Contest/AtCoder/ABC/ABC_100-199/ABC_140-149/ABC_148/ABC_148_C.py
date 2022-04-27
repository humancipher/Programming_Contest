A, B = map(int, input().split())

def gcd(A,B):
    if A < B:
        A, B = B, A
    while A % B > 0:
        r = A % B
        A,B = B,r
    return B

print(A*B//gcd(A,B))
