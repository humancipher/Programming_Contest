N = int(input())
A = list(map(int, input().split(" ")))

num,pt,n_pt,count = 1,-1,0,0
while n_pt < len(A):
    if A[n_pt] == num:
        count += n_pt - pt -1
        pt = n_pt
        num += 1
    n_pt += 1
if pt != -1:
    count += len(A) - pt -1
    print(count)
else:
    print(-1)
