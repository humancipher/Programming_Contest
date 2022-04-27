x,y,z = map(int,input().split())

a = 0
while a*x < y*z:
    a += 1
print(a-1)
