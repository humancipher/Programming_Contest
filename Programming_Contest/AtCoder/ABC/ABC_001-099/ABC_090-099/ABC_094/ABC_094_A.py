a,b,x = map(int,input().split())

if a+b >= x and a <= x and b >= x-a:
    print("YES")
else:
    print("NO")
