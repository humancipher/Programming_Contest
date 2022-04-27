from sys import stdin
input = stdin.readline

def dfs(depth,x,s):
    if depth == 0:
        return s
    else:
        if s == "A":
            if (x // 2**(depth-1)) % 2 == 0:
                return dfs(depth-1,x % 2**(depth-1),"B")
            else:
                return dfs(depth-1,x % 2**(depth-1),"C")
        if s == "B":
            if (x // 2**(depth-1)) % 2 == 0:
                return dfs(depth-1,x % 2**(depth-1),"C")
            else:
                return dfs(depth-1,x % 2**(depth-1),"A")
        if s == "C":
            if (x // 2**(depth-1)) % 2 == 0:
                return dfs(depth-1,x % 2**(depth-1),"A")
            else:
                return dfs(depth-1,x % 2**(depth-1),"B")

def maeshori(depth,s):
    if s == "A":
        if depth % 3 == 0:
            return "A"
        elif depth % 3 == 1:
            return "B"
        else:
            return "C"
    elif s == "B":
        if depth % 3 == 0:
            return "B"
        elif depth % 3 == 1:
            return "C"
        else:
            return "A"
    else:
        if depth % 3 == 0:
            return "C"
        elif depth % 3 == 1:
            return "A"
        else:
            return "B"

def main():
    S = input().rstrip()
    q = int(input())
    Ans = []
    for _ in range(q):
        t,k = map(int,input().split())
        if t <= 60:
            sho = (k-1) // 2**t
            amari = (k-1) % 2**t
        else:
            sho,amari = 0,k-1
        st = S[sho]
        if t > 60:
            st = maeshori(t-60,st)
            t = 60
        Ans.append(dfs(t,amari,st))
    for i in range(len(Ans)):
        print(Ans[i])

if __name__ == "__main__":
    main()
