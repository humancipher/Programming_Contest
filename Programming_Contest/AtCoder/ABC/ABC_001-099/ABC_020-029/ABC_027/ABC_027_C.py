N = int(input())

depth,n = 0,N
while n > 1:
    n //= 2
    depth += 1

x,turn = 1,0
while x <= N:
    if (depth + turn) % 2 == 0:
        x = 2 * x + 1
    else:
        x = 2 * x
    turn += 1

if turn != 0:
    turn -= 1

if turn % 2 == 0:
    print("Aoki")
else:
    print("Takahashi")
