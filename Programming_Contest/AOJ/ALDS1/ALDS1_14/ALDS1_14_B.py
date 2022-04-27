def comp(T,P):
    if T == P:
        return True
    else:
        return False

def main():
    T = input()
    P = input()
    n1,n2 = len(T),len(P)

    for i in range(n1-n2+1):
        if comp(T[i:i+n2],P):
            print(i)

if __name__ == "__main__":
    main()
