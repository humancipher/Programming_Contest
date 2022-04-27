abc = input()
ans = 100*int(abc[0]) + 10*int(abc[1]) + int(abc[2]) + 100*int(abc[1]) + 10*int(abc[2]) + int(abc[0])+ 100*int(abc[2]) + 10*int(abc[0]) + int(abc[1])
print(ans)