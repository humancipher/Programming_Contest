n = int(input())
S1 = [0 for _ in range(n+1)]
S2 = [0 for _ in range(n+1)]
for i in range(n):
    c,p = map(int,input().split())
    if c == 1:
        S1[i+1] = p
    else:
        S2[i+1] = p
for i in range(n):
    S1[i+1] += S1[i]
    S2[i+1] += S2[i]
q = int(input())
for _ in range(q):
    l,r = map(int,input().split())
    ans1 = S1[r] - S1[l-1]
    ans2 = S2[r] - S2[l-1]
    print(ans1,ans2)
