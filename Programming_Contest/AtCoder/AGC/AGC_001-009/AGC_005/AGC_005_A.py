from bisect import bisect_right

def cal(X):
    output = []
    for i in range(len(X)):
        if len(output) > 0:
            if output[len(output)-1] == "S" and X[i] == "T":
                output.pop()
            else:
                output.append(X[i])
        else:
            output.append(X[i])

    return len(output)

def main():
    X = input()
    print(cal(X))

if __name__ == "__main__":
    main()
