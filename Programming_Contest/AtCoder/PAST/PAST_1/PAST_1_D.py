N = int(input())
A = [int(input()) for _ in range(N)]

sum_correct = (N*(N+1))//2
if sum(A) == sum_correct:
    print("Correct")
else:
    A.sort()
    for i in range(1,N):
        if A[i] == A[i-1]:
            ans1 = A[i]
            break
    ans2 = (ans1 - (sum(A) - sum_correct))
    print(ans1,ans2)
