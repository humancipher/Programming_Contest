a,b = map(int,input().split())

if a <= b:
    for i in range(b):
        print(str(a),end="")
    print()
else:
    for i in range(a):
        print(str(b),end="")
    print()
