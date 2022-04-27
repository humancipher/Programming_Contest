N = int(input())
ST = []
for i in range(N):
    ST.append(input().split())
    ST[i][1] = int(ST[i][1])
X = input()

pt = 0
for i in range(N):
    if X == ST[i][0]:
        pt = i
        break

sum = 0
for i in range(pt+1,N):
    sum += ST[i][1]

print(sum)
