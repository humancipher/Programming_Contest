def solve(A,n,k):
    D = dict()
    ans = 0
    left,right = 0,0
    while right < n:
        if len(D) < k:
            if A[right] not in D:
                D[A[right]] = 1
            else:
                D[A[right]] += 1
            ans = max(ans,right - left + 1)
            right += 1
        elif len(D) == k:
            if A[right] in D:
                D[A[right]] += 1
                ans = max(ans,right - left + 1)
                right += 1
            else:
                while len(D) == k:
                    if D[A[left]] == 1:
                        D.pop(A[left])
                    else:
                        D[A[left]] -= 1
                    left += 1
    return ans

n,k = map(int,input().split())
A = list(map(int,input().split()))
print(solve(A, n, k))
