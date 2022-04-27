S = list(input())

def judge(s):
    if s == "A" or s == "C" or s =="G" or s =="T":
        return True
    else:
        return False

pt_l,pt_r,ans = 0,0,0
while pt_r < len(S):
    if judge(S[pt_r]):
        pt_r += 1
    else:
        ans = max(ans,pt_r - pt_l)
        pt_l = pt_r+1
        pt_r = pt_l
ans = max(ans,pt_r - pt_l)
print(ans)
