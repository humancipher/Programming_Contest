from math import sqrt

def main():
    sq = set([i**2 for i in range(1,500)])
    P = [0 for _ in range(1001)]
    #P[i]:a**2+b**2==c**2 and a+b+c==iを満たすiに対するa<=b<=cの個数
    for a in range(1,500):
        for b in range(a,500):
            if a**2 + b**2 in sq:
                c = int(sqrt(a**2 + b**2))
                if a+b+c <= 1000:
                    P[a+b+c] += 1

    ans,tmp_max = 0,0
    for i in range(1,1001):
        if tmp_max < P[i]:
            ans,tmp_max = i,P[i]
    
    print(ans)

if __name__ == "__main__":
    main()
