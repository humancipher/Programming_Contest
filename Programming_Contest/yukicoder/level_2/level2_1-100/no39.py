from copy import copy

n = list(str(int(input())))

ans = int("".join(n))
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if int(n[i]) < int(n[j]):
            tmp = copy(n)
            tmp[i],tmp[j] = tmp[j],tmp[i]
            ans = max(ans,int("".join(tmp)))
print(ans)
