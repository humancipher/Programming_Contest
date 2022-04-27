def dfs(A,n,Use,ans):
    if len(Use) == 0:
        return ans
    else:
        x = Use.pop()
        Y = [0] * len(Use)
        Use2 = [[] for _ in range(len(Use))]
        for i in range(len(Use)):
            for j in range(len(Use)):
                if i != j:
                    Use2[i].append(Use[j])
                else:
                    Y[i] = Use[j]
        ret = 0
        for i in range(len(Y)):
            ret = max(ret,dfs(A,n,Use2[i],ans ^ A[Y[i]][x]))
        return ret
 
def main():
    n = int(input())
    A = [list(map(int,input().split())) for _ in range(2*n-1)]
    for i in range(2*n-1):
        A[i] = [0] * (i+1) + A[i]

    Use = [i for i in range(2*n)]
    ans = dfs(A,n,Use,0)
    print(ans)

if __name__ == "__main__":
    main()
