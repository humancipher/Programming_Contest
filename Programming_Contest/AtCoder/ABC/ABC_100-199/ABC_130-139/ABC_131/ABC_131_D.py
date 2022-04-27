N = int(input())
AB = [tuple(map(int,input().split())) for _ in range(N)]

AB.sort(key = lambda x:x[1])

ans,time,count = True,0,0
while count < N and ans:
	time += AB[count][0]
	if time > AB[count][1]:
		ans = False
	count += 1

if ans:
	print("Yes")
else:
	print("No")
