def mult(a,b):
    #a以上の最小のbの倍数
    d = (a-1)//b
    return b*(d+1)

def mov(CSF,st):
    N = len(CSF)
    time = 0
    for i in range(st,N):
        c,s,f = CSF[i][0],CSF[i][1],CSF[i][2]
        time = max(time,s)
        time = mult(time,f) + c
    return time

def main():
    N = int(input())
    CSF = [list(map(int,input().split())) for _ in range(N-1)]

    for i in range(N-1):
        print(mov(CSF,i))
    print(0)

if __name__ == "__main__":
    main()
