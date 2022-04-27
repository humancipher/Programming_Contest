def judge(s,t):
    return s == t

def solve(s,t):
    if judge(s,t):
        return True
    else:
        for _ in range(len(t)-1):
            s = s[1:] + s[0]
            if judge(s,t):
                return True
        return False

def main():
    s = input()
    t = input()
    if solve(s,t):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
