def cal(A,B,x):
    return int((A*x)/B) - A*int(x/B)

def main():
    A,B,N = map(int,input().split())
    if N <= B-1:
        ans = cal(A,B,N)
    else:
        ans = cal(A,B,B-1)
    print(ans)

if __name__ == "__main__":
    main()
