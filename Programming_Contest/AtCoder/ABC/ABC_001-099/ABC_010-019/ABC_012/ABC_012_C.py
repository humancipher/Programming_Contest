n = int(input())
s = 0
for i in range(1,10):
    for j in range(1,10):
        s += i*j
for i in range(1,10):
    for j in range(1,10):
        if i*j == s - n:
            print(str(i) + " x " + str(j))
