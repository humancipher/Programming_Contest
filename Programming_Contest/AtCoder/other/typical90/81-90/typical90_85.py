def solve(n,bef,rec):
    if rec == 1:
        if n >= bef:
            return 1
        else:
            return 0
    ans = 0
    i = bef
    while i**rec <= n:
        if n % i == 0:
            ans += solve(n//i,i,rec-1)
        i += 1
    return ans

def main():
    k = int(input())
    print(solve(k,1,3))

if __name__ == "__main__":
    main()
