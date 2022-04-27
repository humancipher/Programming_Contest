def judge(s1,s2,s3):
    if (s2[1]-s1[1])*(s3[0]-s1[0]) == (s3[1]-s1[1])*(s2[0]-s1[0]):
        return True
    else:
        return False

def solve(S,N):
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if judge(S[i],S[j],S[k]):
                    return True
    return False

def main():
    N = int(input())
    S = [list(map(int,input().split())) for _ in range(N)]
    if solve(S,N):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
