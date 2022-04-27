N = int(input())
S = input()

def b_search(A,key):
    left,right,diff = 0,len(A),0
    output = False
    count = 0
    while left < right and count < 15:
        mid = (left+right)//2
        if A[mid] == key:
            return True
        elif A[mid] < key:
            left = mid
        else:
            right = mid
        count += 1
        #print(left,mid,right)

R,G,B = [],[],[]

for i in range(N):
    if S[i] == "R":
        R.append(i+1)
    if S[i] == "G":
        G.append(i+1)
    if S[i] == "B":
        B.append(i+1)

if len(R) <= len(G) and len(B) <= len(G):
    G,B = B,G
elif len(G) <= len(R) and len(B) <= len(R):
    R,B = B,R

#最長はB
ans = 0
for i in range(len(R)):
    for j in range(len(G)):
        tmp = 0
        if R[i] < G[j]:
            #b < r < g or r < b < g or r < g < b
            if b_search(B,R[i]-(G[j]-R[i])):
                tmp += 1
            if (G[j]-R[i]) % 2 == 0 and b_search(B,(G[j]+R[i])//2):
                tmp += 1
            if b_search(B,G[j]+(G[j]-R[i])):
                tmp += 1
            ans += len(B)-tmp
        else:
            #b < g < r or g < b < r or g < r < b
            if b_search(B,G[j]-(R[i]-G[j])):
                tmp += 1
            if (R[i]-G[j]) % 2 == 0 and b_search(B,(R[i]+G[j])//2):
                tmp += 1
            if b_search(B,R[i]+(R[i]-G[j])):
                tmp += 1
            ans += len(B)-tmp

print(ans)
