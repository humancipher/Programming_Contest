S = input()

big,small = False,False
T = set()
for i in range(len(S)):
    if 0 <= ord(S[i])-ord("A") < 26:
        big = True
    if 0 <= ord(S[i])-ord("a") < 26:
        small = True
    T.add(S[i])
if big and small and len(T) == len(S):
    print("Yes")
else:
    print("No")