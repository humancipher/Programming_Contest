from collections import Counter

N = int(input())
A = Counter(list(map(int,input().split())))

ans = 0
for a in A:
    if A[a] < a:
        ans += A[a]
    elif A[a] > a:
        ans += A[a] - a

print(ans)
