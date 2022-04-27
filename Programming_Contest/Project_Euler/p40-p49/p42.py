from math import sqrt

def tri(n):
    n *= 2
    n1 = int(sqrt(n))
    if n1*(n1+1) == n:
        return True
    else:
        return False

def s_to_i(s):
    output = 0
    for i in range(len(s)):
        output += (ord(s[i])-64)
    return output

def main():
    path = "./p42_input.txt"

    with open(path) as f:
        L = f.read().split(",")

    for i in range(len(L)):
        L[i] = L[i][1:len(L[i])-1]

    ans = 0
    for l in L:
        if tri(s_to_i(l)):
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
