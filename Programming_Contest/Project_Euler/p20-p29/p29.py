a,b = 100,100

S = set()

for i in range(2,a+1):
    for j in range(2,b+1):
        if pow(i,j) not in S:
            S.add(pow(i,j))

print(len(S))
