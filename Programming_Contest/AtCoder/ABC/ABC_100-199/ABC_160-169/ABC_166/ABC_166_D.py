def cal(a,b):
    return a**5-b**5

def main():
    X = int(input())
    update = True
    for i in range(10**3):
        for j in range(10**3):
            if cal(i,j) == X:
                a,b = i,j
                update = False
                break
            if cal(i,-j) == X:
                a,b = i,-j
                update = False
                break
        if not update:
            break

    print(a,b)

if __name__ == "__main__":
    main()
