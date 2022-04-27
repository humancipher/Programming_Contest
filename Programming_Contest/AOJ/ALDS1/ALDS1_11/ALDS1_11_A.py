N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

class Graph:
    def __init__(self,Vertex,Edge):
        self.V = Vertex
        self.E = Edge

Edge = [i+1 for i in range(N)]
Vertex = []
for i in range(N):
    for j in range(2,A[i][1]+2):
        Vertex.append((A[i][0],A[i][j]))

g = Graph(Vertex,Edge)

R = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if (i+1,j+1) in g.V:
            R[i][j] = 1

for i in range(N):
    for j in range(N):
        if j >= 1:
            print(" ",end="")
        print(R[i][j],end="")
    print()
