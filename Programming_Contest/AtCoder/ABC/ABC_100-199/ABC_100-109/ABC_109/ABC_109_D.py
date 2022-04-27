def line_mainte(A,h):
    output = []
    for i in range(len(A)-1):
        if A[i] % 2 != 0:
            A[i] -= 1
            A[i+1] += 1
            output.append(str(h)+" "+str(i+1)+" "+str(h)+" "+str(i+2))
    return (len(output),output)

def row_mainte(A,w):
    output = []
    for i in range(len(A)-1):
        if A[i] % 2 != 0:
            A[i] -= 1
            A[i+1] += 1
            output.append(str(i+1)+" "+str(w)+" "+str(i+2)+" "+str(w))
    return (len(output),output)

H,W = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(H)]

count,procedure = 0,[]
for i in range(H):
    tmp = line_mainte(a[i],i+1)
    count += tmp[0]
    procedure += tmp[1]
row_W = [a[i][W-1] for i in range(H)]
tmp = row_mainte(row_W,W)
count += tmp[0]
procedure += tmp[1]

print(count)
for i in range(len(procedure)):
    print(procedure[i])
