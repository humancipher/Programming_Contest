from functools import lru_cache
INF = 10**20

@lru_cache(maxsize=None)
def solve(x,y):
    if y <= x+1:
        return abs(y-x)
    if y % 2 == 0:
        return min(abs(y-x),solve(x,y//2)+1)
    else:
        return min(abs(y-x),solve(x,(y+1)//2)+2,solve(x,(y-1)//2)+2)

def main():
    x,y = map(int,input().split())
    print(solve(x,y))

if __name__ == "__main__":
    main()
