N = int(input())
S = input()

pt,pt_c,pt_tmp,ans = 1,S[0],0,1
while pt < N:
    if S[pt] != S[pt_tmp]:
        pt_c = S[pt]
        pt_tmp = pt
        ans += 1
    pt += 1

print(ans)
