N = int(input())

RE = ["AC","WA","TLE","RE"]
cnt = [0,0,0,0]

for i in range(N):
    re = input()
    for j in range(4):
        if re == RE[j]:
            cnt[j] += 1

for j in range(4):
    print(RE[j] + " x " + str(cnt[j]))
