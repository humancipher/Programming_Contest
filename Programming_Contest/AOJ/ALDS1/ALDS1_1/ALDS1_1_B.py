x,y = map(int, input().split())

def GCD(x,y):
    if y > x:
        x,y = y, x
    r = x % y
    while x % y > 0:
        r = x % y
        x = y
        y = r
    return y

print(GCD(x,y))
