from collections import deque

def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    A = [tuple(map(int,input().split())) for _ in range(2)]
    B = [[None] * n for _ in range(2)]
    V = [(0,1),(1,0)]
    Q = deque()
    Q.append((0,0,A[0][0]))
    while len(Q) > 0:
        x,y,now = Q.popleft()
        if B[x][y] == None:
            B[x][y] = now
        else:
            B[x][y] = max(B[x][y],now)
        for vx,vy in V:
            if 0 <= x+vx and x+vx < 2 and 0 <= y+vy and y+vy < n:
                Q.append((x+vx,y+vy,now + A[x+vx][y+vy]))
    print(B[1][n-1])

if __name__ == "__main__":
    main()
