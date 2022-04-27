from itertools import permutations

NML = list(map(int,input().split()))
PQR = list(map(int,input().split()))

L = list(permutations([0,1,2]))

ans = 0
for i in range(len(L)):
    tmp = 1
    for j in range(3):
        tmp *= NML[j] // PQR[L[i][j]]
    ans = max(ans,tmp)

print(ans)
