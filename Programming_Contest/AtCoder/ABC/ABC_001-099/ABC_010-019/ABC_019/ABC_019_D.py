import sys

n = int(input())
farest,maxdist = 1,0
for i in range(2,n+1):
    print ("? {0} {1}".format(1, i))
    sys.stdout.flush()
    dist = int(input())
    if maxdist < dist:
        maxdist = dist
        farest = i
for i in range(1,n+1):
    if farest == i:
        continue
    print ("? {0} {1}".format(farest, i))
    sys.stdout.flush()
    dist = int(input())
    if maxdist < dist:
        maxdist = dist
print("! " + str(maxdist))
