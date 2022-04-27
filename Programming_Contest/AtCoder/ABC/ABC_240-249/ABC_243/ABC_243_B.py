n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans1,ans2 = 0,0
for i in range(n):
    if A[i] == B[i]:
        ans1 += 1
for i in range(n):
    for j in range(n):
        if i != j and A[i] == B[j]:
            ans2 += 1
print(ans1)
print(ans2)