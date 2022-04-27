from math import sqrt

def cal(n,k):
    Div = set()
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            Div.add(n//i)
            Div.add(i)
    output = n
    for a in Div:
        if a <= k:
            output = min(output,n//a)
    return output

def main():
    t = int(input())
    ans = []
    for i in range(t):
        n,k = map(int,input().split())
        ans.append(cal(n,k))

    for i in range(t):
        print(ans[i])

if __name__ == "__main__":
    main()
