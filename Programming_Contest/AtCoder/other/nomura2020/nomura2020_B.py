def cal(T):
    T = list(T)
    for i in range(len(T)-1):
        if T[i] == "P" and T[i+1] == "?":
            T[i+1] = "D"
        if T[i] == "?" and T[i+1] == "D":
            T[i] = "P"
    for i in range(len(T)-1):
        if T[i] == "?" and T[i+1] == "?":
            T[i],T[i+1] = "P","D"
    for i in range(len(T)):
        if T[i] == "?":
            T[i] = "D"
    T = "".join(T)
    return T

def main():
    T = input()

    print(cal(T))

if __name__ == "__main__":
    main()
