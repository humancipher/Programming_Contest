def solve(n):
    D = []
    for i in range(1,n):
        if i**2 <= n:
            if n % i == 0:
                D.append(i)
                if i != n // i and i != 1:
                    D.append(n // i)
        else:
            break
    s = sum(D)
    if s == n:
        return "Perfect"
    elif s < n:
        return "Deficient"
    else:
        return "Abundant"

def main():
    n = int(input())
    print(solve(n))

if __name__ == "__main__":
    main()
