from math import sqrt

N,M = map(int,input().split())

divisor = set([])
for i in range(1,int(sqrt(M))+1):
	if M % i == 0:
		if i <= int(M / N):
			divisor.add(i)
		if (M // i) <= int(M / N):
			divisor.add(M // i)

print(max(divisor))
