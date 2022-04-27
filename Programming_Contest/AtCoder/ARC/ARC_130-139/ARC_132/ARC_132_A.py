n = int(input())
R = list(map(int,input().split()))
C = list(map(int,input().split()))
Ans = []
q = int(input())
for _ in range(q):
    r,c = map(int,input().split())
    if R[r-1] + C[c-1] > n:
        Ans.append("#")
    else:
        Ans.append(".")
print("".join(Ans))