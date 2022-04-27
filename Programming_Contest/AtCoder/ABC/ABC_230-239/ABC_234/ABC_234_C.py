k = int(input())

kb = bin(k)[2:]
Ans = ["0" if kb[i] == "0" else "2" for i in range(len(kb))]
print("".join(Ans))