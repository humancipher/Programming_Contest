X,Y,A,B,C = map(int,input().split())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
R = list(map(int,input().split()))

P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)

ans = sum(P[:X])+sum(Q[:Y])
pt_x,pt_y = X-1,Y-1
for r in range(len(R)):
    if pt_x >= 0 and pt_y >= 0:
        if P[pt_x] < Q[pt_y]:
            if P[pt_x] < R[r]:
                ans = ans + R[r] - P[pt_x]
                pt_x -= 1
        else:
            if Q[pt_y] < R[r]:
                ans = ans + R[r] - Q[pt_y]
                pt_y -= 1
    elif pt_x >= 0:
        if P[pt_x] < R[r]:
            ans = ans + R[r] - P[pt_x]
            pt_x -= 1
        else:
            break
    elif pt_y >= 0:
        if Q[pt_y] < R[r]:
            ans = ans + R[r] - Q[pt_y]
            pt_y -= 1
        else:
            break
    else:
        break

print(ans)
