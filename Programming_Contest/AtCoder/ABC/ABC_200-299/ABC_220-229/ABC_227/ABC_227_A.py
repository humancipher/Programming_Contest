n,k,a = map(int,input().split())

a += k - 2
print(a % n + 1)