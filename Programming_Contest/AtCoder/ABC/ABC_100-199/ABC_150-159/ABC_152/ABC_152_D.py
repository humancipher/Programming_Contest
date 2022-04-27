N = int(input())

C_ab = [[0 for i in range(10)] for j in range(10)]
for i in range(1,N+1):
    C_ab[int(str(i)[0])][int(str(i)[-1])] += 1

count = 0
for i in range(1,10):
    for j in range(1,10):
        count += C_ab[i][j]*C_ab[j][i]

print(count)
