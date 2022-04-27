N = input()

N = N[len(N)-1]

h = set([2,4,5,7,9])
p = set([0,1,6,8])
b = set([3])

if int(N) in h:
    print("hon")
elif int(N) in p:
    print("pon")
else:
    print("bon")
