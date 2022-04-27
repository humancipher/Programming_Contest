from collections import Counter
from itertools import permutations

S = input()
if len(S) >= 4:
    S = Counter(S)
    ans = "No"
    for i in range(992 // 8):        
        if ((i+1) * 8 <= 100):
            continue
        flag = True
        Pat = Counter(list(str((i+1) * 8)))
        for p in Pat:
            if Pat[p] > S[p]:
                flag = False
                break
        if flag:
            ans = "Yes"
            break
    print(ans)
else:
    S = list(permutations(list(S)))
    for j in range(len(S)):
        S[j] = int("".join(S[j]))
    ans = "No"
    for i in range(992 // 8):
        for j in range(len(S)):
            if S[j] == (i+1) * 8:
                ans = "Yes"
                break
    print(ans)
