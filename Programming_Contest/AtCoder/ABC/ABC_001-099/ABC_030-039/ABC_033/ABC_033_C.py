def solve(S):
    cnt = 0
    zero = False
    for i in range(len(S)):
        if S[i] != "+" and S[i] != "*":
            if S[i] == "0":
                zero = True
        elif S[i] == "+":
            if not zero:
                cnt += 1
            else:
                zero = False
        else:
            continue
    if not zero:
        cnt += 1

    return cnt

def main():
    S = input()

    print(solve(S))

if __name__ == "__main__":
    main()
