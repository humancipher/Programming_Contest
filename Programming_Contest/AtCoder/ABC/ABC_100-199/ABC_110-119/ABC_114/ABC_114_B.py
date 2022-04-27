S = input()

diff_min = 1000

for i in range(len(S)-2):
    if diff_min > abs(753 - int(S[i:i+3])):
        diff_min = abs(753 - int(S[i:i+3]))

print(diff_min)
