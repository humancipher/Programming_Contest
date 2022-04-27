N = int(input())
S = [list(input()) for _ in range(N)]

for i in range(N):
	S[i].sort()

for i in range(N):
	S[i] = "".join(S[i])

S.sort()
S.append(None)

pt,count,C = 1,0,[]
while pt <= N:
	if S[pt-1] == S[pt]:
		count += 1
	else:
		if count > 0:
			C.append(count+1)
			count = 0
	pt += 1

ans = 0
for i in range(len(C)):
	ans += C[i]*(C[i]-1) // 2

print(ans)
