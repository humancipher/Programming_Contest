def product(A,B,n):
    #行列A,B(n x n)に対するA x B
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_list(OP,M):
    Mat = [] #M[i]:i回目のクエリ後の行列
    Mat.append([[1,0,0],[0,1,0],[0,0,1]])
    for i in range(M):
        if OP[i][0] == 1:
            Mat_op = [[0,1,0],[-1,0,0],[0,0,1]]
            Mat.append(product(Mat_op,Mat[-1],3))
        elif OP[i][0] == 2:
            Mat_op = [[0,-1,0],[1,0,0],[0,0,1]]
            Mat.append(product(Mat_op,Mat[-1],3))
        elif OP[i][0] == 3:
            Mat_op = [[-1,0,2 * OP[i][1]],[0,1,0],[0,0,1]]
            Mat.append(product(Mat_op,Mat[-1],3))
        elif OP[i][0] == 4:
            Mat_op = [[1,0,0],[0,-1,2 * OP[i][1]],[0,0,1]]
            Mat.append(product(Mat_op,Mat[-1],3))
    return Mat

def main():
    N = int(input())
    XY = [list(map(int,input().split())) for _ in range(N)]
    M = int(input())
    OP = [list(map(int,input().split())) for _ in range(M)]
    Q = int(input())
    AB = [list(map(int,input().split())) for _ in range(Q)]
    
    Mat_list = matrix_list(OP,M)
    
    for q in range(Q):
        Mat = Mat_list[AB[q][0]]
        x0,y0 = XY[AB[q][1]-1][0],XY[AB[q][1]-1][1]
        x = Mat[0][0] * x0 + Mat[0][1] * y0 + Mat[0][2] * 1
        y = Mat[1][0] * x0 + Mat[1][1] * y0 + Mat[1][2] * 1
        print(x,y)

if __name__ == "__main__":
    main()
