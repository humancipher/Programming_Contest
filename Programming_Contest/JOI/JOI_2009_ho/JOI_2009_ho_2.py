#2<=d<=10**9,2<=n<=10**5,1<=m<=10**4
d = int(input())
n = int(input())
m = int(input())
D = [0]
for _ in range(n-1):
    D.append(int(input()))
D.append(d)
D.sort()
K = []
for _ in range(m):
    K.append(int(input()))

def b_search(D,key,left,right):
    #D[pt] <= key < D[pt+1]を満たすptを探索
    if D[left] <= key and D[right] >= key and right-left==1:
        return (left,right)
    else:
        mid = (left+right)//2
        if D[mid] < key:
            return b_search(D,key,mid,right)
        else:
            return b_search(D,key,left,mid)

def dist(D,key):
    scp = b_search(D,key,0,n)
    return min(D[scp[1]]-key,key-D[scp[0]])

dist_sum = 0
for i in range(m):
    dist_sum += dist(D,K[i])
print(dist_sum)
