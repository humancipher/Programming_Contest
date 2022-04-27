S = input()

flag = 0

for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == 'L':
            flag = 1
    elif i % 2 == 1:
        if S[i] == 'R':
            flag = 1

if flag == 0:
    print('Yes')
else:
    print('No')
