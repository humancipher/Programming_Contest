H,N = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(N)]

DP = [0 for i in range(10**4+1)] #DP[h]=体力hのやつを倒す最小mp
#DPのrangeを大きくとることで後々計算が簡単になる

for h in range(1,H+1):
    DP[h] = min((DP[h - a] + b) for a,b in AB )
    #注：h - a < 0の場合もある.
    #　　この場合 -(h - a) >= len(DP) のときにout of rangeになる
    #これを防ぐにはlen(DP)を十分大きくしておけばいい
    #h - a < 0 のときはDP[h-a] = 0に初期化しておくとbだけが消費mpになる

print(DP[H])
