def judge(N):
    for i in range(len(N)):
        if N[i] != N[len(N)-i-1]:
            return False
    return True

def solve(N):
    M = N
    for _ in range(len(N)+1):
        if judge(M):
            return True
        M = "0" + M
    return False

def main():
    N = input()
    if solve(N):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
