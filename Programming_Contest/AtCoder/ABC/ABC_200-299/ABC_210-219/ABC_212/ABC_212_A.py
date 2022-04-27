a,b = map(int,input().split())
if a * b > 0:
    print("Alloy")
elif b == 0:
    print("Gold")
else:
    print("Silver")