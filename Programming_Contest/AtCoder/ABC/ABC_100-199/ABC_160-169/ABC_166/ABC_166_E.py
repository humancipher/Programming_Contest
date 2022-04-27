from bisect import bisect_left,bisect_right

N = int(input())
A = list(map(int,input().split()))

diff_AB = [(i+1-A[i]) for i in range(N)]
diff_AB.sort()

ans = 0
for i in range(N):
    ans += (bisect_right(diff_AB,A[i]+i+1)- bisect_left(diff_AB,A[i]+i+1))

print(ans)
