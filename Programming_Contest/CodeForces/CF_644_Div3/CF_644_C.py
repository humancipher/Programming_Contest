def similar(A,N):
    Odd,Even = [],[]
    for i in range(N):
        if A[i] % 2 == 0:
            Even.append(A[i])
        else:
            Odd.append(A[i])
    if len(Odd) % 2 == 0:
        return "YES"
    else:
        Odd = set(Odd)
        for i in range(len(Even)):
            if Even[i]-1 in Odd or Even[i]+1 in Odd:
                return "YES"
        return "NO"

def main():
    T = int(input())
    ans = []
    for i in range(T):
        N = int(input())
        a = list(map(int,input().split()))

        ans.append(similar(a,N))

    for i in range(T):
        print(ans[i])

if __name__ == "__main__":
    main()
