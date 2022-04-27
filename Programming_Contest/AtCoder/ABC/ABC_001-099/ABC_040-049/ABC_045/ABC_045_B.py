S = [input() for _ in range(3)]

turn = 0
Next = {"a":0,"b":1,"c":2}
Winner = ["A","B","C"]
while True:
    if len(S[turn]) > 0:
        next_turn = Next[S[turn][0]]
        S[turn] = S[turn][1:]
    else:
        print(Winner[turn])
        break
    turn = next_turn
