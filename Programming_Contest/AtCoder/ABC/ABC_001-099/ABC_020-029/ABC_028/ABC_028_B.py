S = input()

Count = [0 for _ in range(6)]

for i in range(len(S)):
    Count[ord(S[i])-65] += 1

ans = " ".join(map(str,Count))
print(ans)
