def judge(a,s):
    digit = 0
    Used = []
    while a > 0:
        if a % 2 != 0:
            s -= 2 * 2**digit
            Used.append(digit)
        a //= 2
        digit += 1
    if s < 0:
        return False
    for u in Used:
        if s & 2**u != 0:
            return False
    return True

def main():
    import sys
    sys.stdin.readline
    t = int(input())
    Ans = []
    for _ in range(t):
        a,s = map(int,input().split())
        if judge(a,s):
            Ans.append("Yes")
        else:
            Ans.append("No")
    for i in range(t):
        print(Ans[i])

if __name__ == "__main__":
    main()
