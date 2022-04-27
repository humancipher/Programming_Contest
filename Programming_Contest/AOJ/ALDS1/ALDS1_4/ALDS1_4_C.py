n = int(input())
C = [input().split() for _ in range(n)]
D = set()
for i in range(n):
    c,s = C[i][0],C[i][1]
    if c == "insert":
        D.add(s)
    else:
        if s in D:
            print("yes")
        else:
            print("no")
