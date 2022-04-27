def operate(S,T):
    S.sort(reverse = True)
    x,y = 0,0
    for i in range(len(S)):
        if S[i] == "L":
            x -= 1
        if S[i] == "R":
            x += 1
        if S[i] == "U":
            y += 1
        if S[i] == "D":
            y -= 1
        if S[i] == "?":
            if T == 1:
                if x >= 0:
                    x += 1
                else:
                    x -= 1
            else:
                if x == 0 and y == 0:
                    x += 1
                elif x > 0:
                    x -= 1
                elif x < 0:
                    x += 1
                elif y > 0:
                    y -= 1
                else:
                    y += 1

    return abs(x)+abs(y)

def main():
    S = list(input())
    T = int(input())

    print(operate(S,T))

if __name__ == "__main__":
    main()
