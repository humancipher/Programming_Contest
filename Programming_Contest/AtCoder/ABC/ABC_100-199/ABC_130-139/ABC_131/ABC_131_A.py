S=input()
flag=0

for i in range(3):
	if S[i]==S[i+1]:
		flag=1
		break

if flag==0:
	print('Good')
else:
	print('Bad')

