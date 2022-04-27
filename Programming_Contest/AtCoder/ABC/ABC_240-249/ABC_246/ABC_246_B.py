from math import sqrt
a,b = map(int,input().split())
x,y = a/sqrt(a**2+b**2),b/sqrt(a**2+b**2)
print(x,y)