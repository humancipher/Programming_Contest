def trib(n):
    M = 10007
    T = [0,0,1]
    while len(T) < n:
        T.append((T[len(T)-1]+T[len(T)-2]+T[len(T)-3]) % M)
    return T[n-1]

def main():
    n = int(input())
    ans = trib(n)
    print(ans)

if __name__ == "__main__":
    main()
