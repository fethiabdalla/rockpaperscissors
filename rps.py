print("Welcome to this epic battle of Rock, Paper, Scissors!")
print()
choice = input("Would you like to play Rock, Paper, Scissors? ")
while choice == "no":
  print()
  break
counter1 = 0
counter2 = 0
while choice == "yes":
    print()
    Player_1 = input("Select your move (R, P or S): ")
    print()
    Player_2 = input("Select your move (R, P or S): ")
    print()
    if Player_1 == "R" and Player_2 == "S":
        print()
        print("Player 1's rock smashed Player 2's scissors!")
        print()
        counter1 += 1
        print("Player 1 has", counter1)
        if counter1 != 3:
          continue
        else:
          print()
          print("You have won 3 rounds of rock, paper, scissors!")
          print()
          break
    elif Player_1 == "R" and Player_2 == "P":
        print()
        print("Player 2's paper smothered Player 1's rock!")
        print()
        counter2 += 1
        print("Player 2 has", counter2)
        if counter2 != 3:
          continue
        else:
          print()
          print("You have won 3 rounds of rock, paper, scissors!")
          print()
          break
    elif Player_1 == "P" and Player_2 == "R":
        print()
        print("Player 1's paper smothered Player 2's rock!")
        print()
        counter1 += 1
        print("Player 1 has", counter1)
        if counter1 != 3:
          continue
        else:
          print()
          print("You have won 3 rounds of rock, paper, scissors!")
          print()
          break
    elif Player_1 == "P" and Player_2 == "S":
        print()
        print("Player 2's scissors cut Player 1's paper!")
        print()
        counter2 += 1
        print("Player 2 has", counter2)
        if counter2 != 3:
          continue
        else:
          print()
          print("You have won 3 rounds of rock, paper, scissors!")
          print()
          break
    elif Player_1 == "S" and Player_2 == "R":
        print()
        print("Player 2's rock smashed Player 1's scissors!")
        print()
        counter2 += 1
        print("Player 2 has", counter2)
        if counter2 != 3:
          continue
        else:
          print()
          print("You have won 3 rounds of rock, paper, scissors!")
          print()
          break
    elif Player_1 == "S" and Player_2 == "P":
        print()
        print("Player 1's scissors cut Player 2's paper!")
        print()
        counter1 += 1
        print("Player 1 has", counter1)
        if counter1 != 3:
          continue
        else:
          print()
          print("You have won 3 rounds of rock, paper, scissors!")
          print()
          break
    elif Player_1 == "R" and Player_2 == "R" or Player_1 == "P" and Player_2 == "P" or Player_1 == "S" and Player_2 == "S":
        print()
        print("Well it's a draw since we picked the same thing...")
        print()
        continue
