N = int(input())
S = [input() for _ in range(N)]

S.sort()

max = 0
Output = []
pt = 0
while pt < N:
    st,tmp = S[pt],0
    while pt < N and st == S[pt]:
        pt += 1
        tmp += 1
        if max == tmp:
            Output.append(st)
        if max < tmp:
            max = tmp
            Output.clear()
            Output.append(st)

for i in range(len(Output)):
    print(Output[i])
