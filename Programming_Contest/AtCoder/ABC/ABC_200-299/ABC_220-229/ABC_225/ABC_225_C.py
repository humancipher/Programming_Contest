n,m = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(n)]
if m > 7:
    ans = "No"
else:
    ans = "Yes"
    left = B[0][0]
    tmp = left
    for j in range(1,m):
        if (tmp-1) % 7 >= (B[0][j]-1) % 7 or tmp >= B[0][j]:
            ans = "No"
            break
        else:
            tmp = B[0][j]
    if ans == "Yes" and n > 1:
        if (B[1][0] - left) % 7 != 0 or B[1][0] <= left:
            ans = "No"
        if ans == "Yes":
            for i in range(1,n):
                tmp_shodiff = (B[i][0]-left) // 7
                for j in range(m):
                    if B[i][j] % 7 != B[0][j] % 7 or (B[i][j] - B[0][j])//7 != tmp_shodiff:
                        ans = "No"
                        break
print(ans)
