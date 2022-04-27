def judge(s,t):
    if s == t:
        return "same"
    else:
        same = True
        for i in range(3):
            if abs(ord(s[i]) - ord(t[i])) != 0 \
            and abs(ord(s[i]) - ord(t[i])) != 32:
                same = False
                break
        if same:
            return "case-insensitive"
        else:
            return "different"

def main():
    s = input()
    t = input()

    print(judge(s,t))

if __name__ == "__main__":
    main()
