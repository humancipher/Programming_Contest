def solve(xy):
    xy_diff = [] # x-yを追加(右上と左下でソートしたい)
    xy_dist = [] # x+yを追加(原典からの距離でソートしたい)
    for x,y in xy:
        xy_diff.append([x,y,x-y])
        xy_dist.append([x,y,x+y])
    xy_diff.sort(key = lambda x:x[2])
    xy_dist.sort(key = lambda x:x[2])

    return max(xy_diff[-1][2] - xy_diff[0][2], xy_dist[-1][2] - xy_dist[0][2])

def main():
    N = int(input())
    xy = [list(map(int,input().split())) for _ in range(N)]
    print(solve(xy))

if __name__ == "__main__":
    main()
