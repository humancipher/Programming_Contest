path = "./p18_input.txt"

with open(path) as f:
    T = []
    for f_line in f:
        T.append(list(map(int,f_line.split())))

N = len(T)

def path_search(T,N):
    for i in reversed(range(N-1)):
        for j in range(i+1):
            T[i][j] += max(T[i+1][j],T[i+1][j+1])

    return T[0][0]

ans = path_search(T,N)
print(ans)
