a,b = map(int,input().split())

if a == b:
    print(2*a)
else:
    c = max(a,b)
    print(2*c-1)
