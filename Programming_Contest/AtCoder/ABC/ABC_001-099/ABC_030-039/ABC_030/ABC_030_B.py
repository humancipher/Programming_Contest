n,m = map(int,input().split())

kaku_n,kaku_m = 30 * (n % 12) + 0.5 * m,6 * (m % 60)

diff = abs(kaku_n - kaku_m)

print(min(diff,360-diff))
