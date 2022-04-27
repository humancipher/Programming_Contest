X,N = map(int,input().split())
P = set(map(int,input().split()))

diff = 0
while True:
    if X - diff not in P:
        print(X - diff)
        break
    elif X + diff not in P:
        print(X + diff)
        break
    else:
        diff += 1
