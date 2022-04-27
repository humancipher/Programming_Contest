N = int(input())
H = list(map(int, input().split(" ")))

if N>1:
	flag=0
	for i in reversed(range(1,N)):
	#逆順で考えれば分かりやすくなったこと
	#逆順の場合はreversed関数を使えばいいこと
	#逆順でrangeが少し違うときは特に注意が必要なこと
	#以上を教訓としよう
		if H[i-1]-H[i]>1:
			flag=1
		if H[i-1]-H[i]==1:
			H[i-1] -= 1
	if flag==0:
		print("Yes")
	else:
		print("No")
else:
	print("Yes")
