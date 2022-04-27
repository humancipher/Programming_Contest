def judge(n,D): #nに嫌いな文字が含まれるかどうか
    L = str(n)
    for d in D:
        if d in L:
            return False
    return True

def solve(N,D):
    for n in range(N,10**6+1):
        if judge(n,D):
            return n

def main():
    N,K = map(int,input().split())
    D = input().split()
    print(solve(N,D))

if __name__ == "__main__":
    main()
