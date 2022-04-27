n = int(input())
A = list(map(int,input().split()))

S = set()
ans = 0
left,right = 0,0
while right < n:
    if A[right] not in S:
        S.add(A[right])
        right += 1
    else:
        S.discard(A[left])
        left += 1
    ans = max(ans,right-left)
print(ans)