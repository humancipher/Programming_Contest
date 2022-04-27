N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

count = 0
rem = 0	#余剰戦力
for i in range(N):
	if A[i]>=B[i]+rem:
		count += B[i]+rem
		rem = 0
	else:
		count += A[i]
		if (B[i]+rem-A[i])>A[i+1]:
			rem = A[i+1]
		else:
			rem = B[i]+rem-A[i]
count += rem #N+1番目の街

print(count)