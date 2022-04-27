a = list(map(int, input().split(" ")))
K=a[0]
X=a[1]

tmp=K
while tmp>1:
	print(X-tmp+1, end=" ")
	tmp -= 1
print(X, end=" ")
tmp=1
while tmp<K:
	print(X+tmp, end=" ")
	tmp += 1
