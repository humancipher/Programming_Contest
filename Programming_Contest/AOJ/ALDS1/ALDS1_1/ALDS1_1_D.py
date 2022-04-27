n = int(input())
R = []
for i in range(n):
    R.append(int(input()))

def maxR(R):
    n = len(R)
    maxv = R[1] - R[0]
    minv = R[0]
    for i in range(1,n):
        maxv = max(maxv, R[i] - minv)
        minv = min(minv, R[i])
    return maxv

print(maxR(R))
