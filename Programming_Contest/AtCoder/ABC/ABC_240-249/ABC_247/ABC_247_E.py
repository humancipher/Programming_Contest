n,x,y = map(int,input().split())
A = list(map(int,input().split()))

B = [[]]
for i in range(n):
    if y <= A[i] <= x:
        B[-1].append(A[i])
    else:
        B.append([])
C = []
for i in range(len(B)):
    if len(B[i]) > 0:
        C.append(B[i])
B = C
ans = 0
if x == y:
    for i in range(len(B)):
        lb = len(B[i])
        ans += (lb*(lb+1))//2
else:
    for i in range(len(B)):
        Bi = B[i]
        lb = len(B[i])
        cx,cy = 0,0
        left,right = 0,0
        if Bi[left] == x:
            cx += 1
        if Bi[left] == y:
            cy += 1
        while left < lb:
            while right < lb:
                if cx == 0 or cy == 0:
                    right += 1
                    if right < lb:
                        if Bi[right] == x:
                            cx += 1
                        if Bi[right] == y:
                            cy += 1
                else:
                    ans += (lb-right)
                    break
            if Bi[left] == x:
                cx -= 1
            if Bi[left] == y:
                cy -= 1
            left += 1
print(ans)