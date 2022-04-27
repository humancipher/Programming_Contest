def read_pt(y,x,vy,vx,read):
    if len(read) == 4:
        return read
    else:
        if x < 0:
            x = 1
            vx *= -1
        if x > 8:
            x = 7
            vx *= -1
        if y < 0:
            y = 1
            vy *= -1
        if y > 8:
            y = 7
            vy *= -1
        read.append([y,x])
        return read_pt(y+vy,x+vx,vy,vx,read)

def main():
    xyW = list(input().split())
    C = [input() for _ in range(9)]

    x,y,W = int(xyW[0])-1,int(xyW[1])-1,xyW[2]
    vx,vy = 0,0
    for i in range(len(W)):
        if W[i] == "R":
            vx = 1
        if W[i] == "L":
            vx = -1
        if W[i] == "U":
            vy = -1
        if W[i] == "D":
            vy = 1

    read = read_pt(y,x,vy,vx,[])

    ans = ""
    for i in range(4):
        ans += C[read[i][0]][read[i][1]]

    print(ans)

if __name__ == "__main__":
    main()
