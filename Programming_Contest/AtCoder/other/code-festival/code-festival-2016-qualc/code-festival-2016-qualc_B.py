def min_day(A,K,T):
    if T == 1:
        return K-1
    else:
        A_max = max(A)
        if A_max <= K - A_max:
            return 0
        else:
            return K-2*(K-A_max)-1

def main():
    K,T = map(int,input().split())
    A = list(map(int,input().split()))

    print(min_day(A,K,T))

if __name__ == "__main__":
    main()
