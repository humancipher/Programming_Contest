l,r = map(int,input().split())
S = list(input())
for i in range((r-l)//2+1):
    S[l+i-1],S[r-i-1] = S[r-i-1],S[l+i-1]
print("".join(S))