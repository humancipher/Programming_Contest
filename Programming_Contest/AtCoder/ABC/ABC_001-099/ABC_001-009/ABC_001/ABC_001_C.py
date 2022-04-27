def sishagonyu(x):
    x *= 10
    if x - int(x) >= 0.5:
        return (int(x) + 1) / 10
    else:
        return int(x) / 10

def main():
    a,b = map(int,input().split())

    a *= 10
    a += 1125
    a %= 36000
    D = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    dir = D[a // 2250]
    fusoku = sishagonyu(b / 60)
    if fusoku <= 0.2:
        furyoku = 0
    elif fusoku <= 1.5:
        furyoku = 1
    elif fusoku <= 3.3:
        furyoku = 2
    elif fusoku <= 5.4:
        furyoku = 3
    elif fusoku <= 7.9:
        furyoku = 4
    elif fusoku <= 10.7:
        furyoku = 5
    elif fusoku <= 13.8:
        furyoku = 6
    elif fusoku <= 17.1:
        furyoku = 7
    elif fusoku <= 20.7:
        furyoku = 8
    elif fusoku <= 24.4:
        furyoku = 9
    elif fusoku <= 28.4:
        furyoku = 10
    elif fusoku <= 32.6:
        furyoku = 11
    else:
        furyoku = 12
    if furyoku == 0:
        print("C 0")
    else:
        print(dir,furyoku)

if __name__ == "__main__":
    main()
