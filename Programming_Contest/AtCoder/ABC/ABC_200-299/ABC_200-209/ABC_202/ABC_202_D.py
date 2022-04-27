from math import factorial

def kaijo(a,b):
    return factorial(a+b) //factorial(a) // factorial(b)

def solve(a,b,k,ans):
    if a == 0:
        return ans + "b" * b
    if b == 0:
        return ans + "a" * a
    if k <= kaijo(a-1,b):
        return solve(a-1,b,k,ans + "a")
    else:
        return solve(a,b-1,k-kaijo(a-1,b),ans + "b")

def main():
    a,b,k = map(int,input().split())
    print(solve(a,b,k,""))

if __name__ == "__main__":
    main()
