H = int(input())
Heap = list(map(int,input().split()))
Heap = ["dummy"] + Heap

def Node_property(Heap):
    L = ["dummy"]
    for i in range(1,H+1):
        key,par,left,right = Heap[i],None,None,None
        if i//2 != 0:
            par = Heap[i//2]
        if 2*i < H+1:
            left = Heap[2*i]
        if 2*i+1 < H+1:
            right = Heap[2*i+1]
        L.append([key,par,left,right])
    return L

Ans = Node_property(Heap)
for i in range(1,H+1):
    print("node "+str(i)+": key = "+str(Ans[i][0])+", ",end="")
    for j in range(1,4):
        if Ans[i][j] != None:
            if j == 1:
                print("parent key = ",end="")
            if j == 2:
                print("left key = ",end="")
            if j == 3:
                print("right key = ",end="")
            print(str(Ans[i][j])+", ",end="")
    print()
