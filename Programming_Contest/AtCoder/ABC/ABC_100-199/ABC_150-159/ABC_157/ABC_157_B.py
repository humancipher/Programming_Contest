A = [list(map(int,input().split())) for _ in range(3)]
N = int(input())
B = []
for _ in range(N):
    B.append(int(input()))

C = [[0 for i in range(3)] for j in range(3)]

for k in range(N):
    for i in range(3):
        for j in range(3):
            if A[i][j] == B[k]:
                A[i][j] = 101

flag = 0
for i in range(3):
    for j in range(3):
        if A[0][0]*A[0][1]*A[0][2] == 101**3 \
        or A[1][0]*A[1][1]*A[1][2] == 101**3 \
        or A[2][0]*A[2][1]*A[2][2] == 101**3 \
        or A[0][0]*A[1][0]*A[2][0] == 101**3 \
        or A[0][1]*A[1][1]*A[2][1] == 101**3 \
        or A[0][2]*A[1][2]*A[2][2] == 101**3 \
        or A[0][0]*A[1][1]*A[2][2] == 101**3 \
        or A[2][0]*A[1][1]*A[0][2] == 101**3:
            flag = 1
            break

if flag == 1:
    print("Yes")
else:
    print("No")
