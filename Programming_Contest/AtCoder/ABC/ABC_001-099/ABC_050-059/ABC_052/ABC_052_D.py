def move(X,N,A,B):
    output = 0
    for i in range(N-1):
        output += min(A*(X[i+1]-X[i]),B)

    return output

def main():
    N,A,B = map(int,input().split())
    X = list(map(int,input().split()))

    print(move(X,N,A,B))

if __name__ == "__main__":
    main()
