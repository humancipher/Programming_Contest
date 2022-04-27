p = int(input())
for _ in range(p):
    n,k = map(int,input().split())
    if (n-1) % (k+1) == 0:
        print("Lose")
    else:
        print("Win")
