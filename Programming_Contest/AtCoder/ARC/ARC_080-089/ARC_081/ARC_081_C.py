N = int(input())
A = list(map(int,input().split()))

A.sort(reverse = True)
A.append(0)

B = [0,0]
cnt,pt = 0,0
while cnt < 2 and pt < N:
    if A[pt] == A[pt+1]:
        B[cnt] = A[pt]
        pt += 2
        cnt += 1
    else:
        pt += 1

print(B[0] * B[1])
