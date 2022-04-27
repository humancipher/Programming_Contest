A = list(map(int,input().split()))

Sum = []
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            Sum.append(A[i]+A[j]+A[k])

Sum.sort(reverse = True)
print(Sum[2])
