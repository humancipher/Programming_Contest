K = int(input())

R = ["1","2","3","4","5","6","7","8","9"]

len_R_p,len_R_n,digit = 0,9,0
while len_R_n < K:
    for i in range(len_R_p,len_R_n):
        if R[i][digit] == "0":
            R.append(R[i]+"0")
            R.append(R[i]+"1")
        elif R[i][digit] == "9":
            R.append(R[i]+"8")
            R.append(R[i]+"9")
        else:
            R.append(R[i]+str(int(R[i][digit])-1))
            R.append(R[i]+str(int(R[i][digit])))
            R.append(R[i]+str(int(R[i][digit])+1))
    len_R_p = len_R_n
    len_R_n = len(R)
    digit += 1

print(R[K-1])
