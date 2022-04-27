n = int(input())
S = set()
for i in range(1,n+1):
    if i**2 <= n:
        if n % i == 0:
            S.add(n//i)
            S.add(i)
    else:
        break
S = list(S)
S.sort()
for i in range(len(S)):
    print(S[i])
