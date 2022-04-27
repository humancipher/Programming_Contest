def rev(amd,goal,N,L):
    for i in range(L//2):
        amd[i],amd[-1-i] = amd[-1-i],amd[i]

    for i in range(L):
        amd[i] = "| " + amd[i] + " |"
    goal = goal.find("o")+2

    for i in range(L):
        if amd[i][goal-1] == "-":
            goal -= 2
        elif amd[i][goal+1] == "-":
            goal += 2

    return goal//2

def main():
    N,L = map(int,input().split())
    amd = [input() for _ in range(L)]
    goal = input()

    print(rev(amd,goal,N,L))

if __name__ == "__main__":
    main()
