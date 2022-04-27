n,p,q = map(int,input().split())
A = list(map(int,input().split()))

for i in range(n):
    A[i] %= p

ans = 0
for i1 in range(n):
    for i2 in range(i1+1,n):
        for i3 in range(i2+1,n):
            for i4 in range(i3+1,n):
                for i5 in range(i4+1,n):
                    tmp = A[i1]
                    tmp = (tmp * A[i2]) % p
                    tmp = (tmp * A[i3]) % p
                    tmp = (tmp * A[i4]) % p
                    tmp = (tmp * A[i5]) % p
                    if tmp == q:
                        ans += 1
print(ans)
