def pali(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            return False
    return True

def rev(n):
    n = list(str(n))
    for i in range(len(n)//2):
        n[i],n[-i-1] = n[-i-1],n[i]
    n = int("".join(n))
    return n

def Lychrel(n):
    cnt = 0
    while cnt < 50:
        n += rev(n)
        cnt += 1
        if pali(n):
            return False
    return True

def main():
    ans = 0
    for i in range(1,10**4):
        if Lychrel(i):
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
