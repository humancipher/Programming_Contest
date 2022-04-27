a,b = map(int,input().split())

a = (a-2)%13
b = (b-2)%13

if a > b:
    print("Alice")
elif a < b:
    print("Bob")
else:
    print("Draw")
