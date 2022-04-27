S = input()
amax,amin = S,S
for i in range(len(S)):
    S = S[1:] + S[0]
    if amax < S:
        amax = S
    if amin > S:
        amin = S
print(amin)
print(amax)
