def Ryuka(n):
    L = [2,1]
    for i in range(n-1):
        L.append(L[len(L)-1]+L[len(L)-2])

    return L[len(L)-1]

def main():
    N = int(input())
    print(Ryuka(N))

if __name__ == "__main__":
    main()
