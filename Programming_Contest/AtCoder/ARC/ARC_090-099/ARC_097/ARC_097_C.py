S = set()
s = input()
k = int(input())

for i in range(len(s)):
    for j in range(1,6):
        if i+j <= len(s):
            S.add(s[i:i+j])
S = list(S)
S.sort()
print(S[k-1])
