N,K = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N-1):
	A[i+1] += A[i]

def b_search(A,a,K):
	#A[i]-a >= Kを満たすiの個数
	if A[0]-a >= K:
		return N
	if A[N-1]-a < K:
		return 0
	left,right = 0,N
	while left < right:
		mid = (left+right)//2
		if A[mid]-a < K and A[mid+1]-a >= K:
			return N-mid-1
		elif A[mid]-a >= K:
			right = mid
		else:
			left = mid

ans = 0
ans += b_search(A,0,K)
for i in range(N-1):
	ans += b_search(A,A[i],K)

print(ans)
