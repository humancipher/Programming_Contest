def digitsum(n):
    ans = 0
    n = str(n)
    for i in range(len(n)):
        ans += int(n[i])
    return ans

def solve(n,k):
    C,C_set = [n],set([n])
    for i in range(k):
        n = (n + digitsum(n)) % 10**5
        if n not in C_set:
            C_set.add(n)
            C.append(n)
        else:
            for i in range(len(C)):
                if C[i] == n:
                    pt = i
                    break
            shuki = len(C) - pt
            k -= pt
            return C[pt + (k % shuki)]

    return C[-1]

def main():
    n,k = map(int,input().split())
    print(solve(n,k))

if __name__ == "__main__":
    main()
