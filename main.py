player1 = int(input("Games won by A: "))
player2 = int(input("Games won by B: "))

if ((player1 >= 6 and player1<=7) and player1 - player2 >= 2) or (player1 == 7 and player2 > 5)or (player1 == 7 and player2 == 6):
    print("A won the set")
elif ((player2 >= 6 and player2<=7) and player2 - player1 >= 2)and (player2 == 7 and player1 >= 5) or (player2 == 7 and player1 == 6):
    print("B won the set")
elif (player1 > 7 or player2 > 7) or (player1 == 7 and player2 < 6) or (player2 == 7 and player1 <6):
    print("Invalid result")
else:
    print("The set is not over yet")