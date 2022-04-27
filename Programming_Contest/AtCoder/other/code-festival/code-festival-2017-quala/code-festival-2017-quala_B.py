N,M,K = map(int,input().split())

ans = "No"
for i in range(N+1):
    for j in range(M+1):
        black = i*M + j*N -2*i*j
        if black == K:
            ans = "Yes"
            break
    if ans == "Yes":
        break

print(ans)
