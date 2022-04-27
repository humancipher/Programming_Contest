n = int(input())
money = int(1.08 * n)
if money < 206:
    print("Yay!")
elif money == 206:
    print("so-so")
else:
    print(":(")
