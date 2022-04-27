a,b = map(int,input().split())

if 0 >= a and b >= 0:
    print("Zero")
elif a > 0:
    print("Positive")
elif (b-a) % 2 == 0:
    print("Negative")
else:
    print("Positive")
