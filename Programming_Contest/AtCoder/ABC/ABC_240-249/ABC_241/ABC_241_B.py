n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = True
for i in range(m):
    flag = False
    for j in range(n):
        if A[j] == B[i]:
            flag = True
            A[j] = 10**10
            break
    if not flag:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")