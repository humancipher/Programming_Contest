def judge(C,n):
    cnt = 0
    for i in range(n):
        if C[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

def solve(n):
    Ans = []
    for i in range(2**n):
        Tmp = []
        for j in range(n):
            if 2**j & i:
                Tmp.append("(")
            else:
                Tmp.append(")")
        if judge(Tmp,n):
            Ans.append("".join(Tmp))
    Ans.sort()
    return Ans

def main():
    n = int(input())
    if n % 2 == 0:
        Ans = solve(n)
        for i in range(len(Ans)):
            print(Ans[i])

if __name__ == "__main__":
    main()

