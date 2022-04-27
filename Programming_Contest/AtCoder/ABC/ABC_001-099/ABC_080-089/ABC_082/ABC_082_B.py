S = list(input())
T = list(input())
S.sort()
T.sort()
for i in range(len(T)//2):
    T[i],T[len(T)-1-i] = T[len(T)-1-i],T[i]
S = "".join(S)
T = "".join(T)
if S < T:
    print("Yes")
else:
    print("No")