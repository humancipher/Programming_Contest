def solve(C,N):
    A,B = [0],[0]
    for i in range(1,N):
        A.append(C[i][0]-C[0][0])
        B.append(C[0][i]-C[0][0])
    amin,bmin = 0,0
    for i in range(N):
        amin = min(amin,A[i])
        bmin = min(bmin,B[i])
    if amin < 0:
        for i in range(N):
            A[i] -= amin
    if bmin < 0:
        for i in range(N):
            B[i] -= bmin
    diff = C[0][0]-(A[0]+B[0])
    possible = True
    for i in range(N):
        for j in range(N):
            if diff != C[i][j]-(A[i]+B[j]):
                possible = False
                break
        if not possible:
            break
    if possible:
        for i in range(N):
            A[i] += diff
        print("Yes")
        print(" ".join(map(str,A)))
        print(" ".join(map(str,B)))
    else:
        print("No")

def main():
    N = int(input())
    C = [list(map(int,input().split())) for _ in range(N)]
    solve(C,N)

if __name__ == "__main__":
    main()
