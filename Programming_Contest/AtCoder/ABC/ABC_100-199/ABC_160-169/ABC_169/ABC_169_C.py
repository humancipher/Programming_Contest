a,b = input().split()

a,b = int(a),str(b)
b = int(b[0] + b[2:])

print(int(a*b)//100)
