from collections import Counter

def make_xor_sum(A):
    #N = len(A)
    #A[0] ^ A[1] == A[2] and A[1] ^ A[2] == A[3] and ...
    #and A[N-2] ^ A[N-1] == A[0] and A[N-1] ^ A[0] == A[1]
    #ならばA[0] ^ A[1] ^ ... ^A[N-1] == 0
    #左辺でA[i]がそれぞれ2回ずつ出てくるから
    output = A[0]
    for i in range(1,len(A)):
        output = output ^ A[i]

    if output == 0:
        return True
    else:
        return False

def main():
    N = int(input())
    a = list(map(int,input().split()))

    if make_xor_sum(a):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
