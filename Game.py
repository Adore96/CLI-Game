from random import randint

player = input('Rock(r) , paper(p) , Scissors(s) ? ')


chosen = randint(1, 3)
# print(chosen)

if chosen == 1:
    computer = 'r'
elif chosen == 2 :
    computer = 'p'
else:
    computer = 's'

print(player, ' Vs ' , computer)

# print(computer)

if computer == player :
    print('DRAW')
elif computer == 'r' and player == 'p' :
    print('Player wins')
elif computer == 'r' and player == 's' :
    print('Computer Wins')
elif computer == 'p' and player == 'r' :
    print('Computer Wins')
elif computer == 'p' and player == 's' :
    print('Player Wins')
elif computer == 's' and player == 'r' :
    print('Player Wins')
elif computer == 's' and player == 'p' :
    print('Computer Wins')
else:
    print('Something has went wrong please try again later')