a,b = map(int,input().split())
c,d = map(int,input().split())

if a == c and b == d:
    ans = 0
elif a + b == c + d or a - b == c - d or abs(a-c) + abs(b-d) <= 3:
    ans = 1
elif (a+b) % 2 == (c+d) % 2 or abs(abs(a-c) - abs(b-d)) <= 3:
    ans = 2
else:
    ans = 3

print(ans)
