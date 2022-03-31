import time

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#number1
letter_to_points = {key:val for key, val in zip(letters, points)}

#number2
letter_to_points[" "] = 0

#number3, 4, 5, 6
def score_word(word):
  point_total = 0
  for i in word:
    point_total += letter_to_points.get(i.upper(), 0)
  return point_total

#number7
brownie_points = score_word("BROWNIE")

#number8
#print(brownie_points)

#number9
players_to_words = {}

#number 10
players_to_points = {}

#number 11, 12, 13 and bits of 15
def update_point_totals(prnt = 'Yes'):
  for player, words in players_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    players_to_points.update({player:player_points})
    if prnt == 'Yes':
      print(f'{player} has {player_points} points')
    else:
      continue
#update_point_totals()
#number 14
#print(players_to_points)

#number 15
def play_word(player, word):
  if players_to_points.get(player) != None:
    players_to_words[player] = players_to_words[player] + [word]
  else:
    players_to_words.update({player:[word]})

guide =  '''
A - Add word to players name, if player is new then it makes a player profile

B - Update and print the new points per player

C - Updates the points and prints the current ranks

D - Prints the number of points for each letter

E - Prints the words played by each player

F - Clears all names and points

-Type either A, b, C or D and press enter
'''

def print_ranks(players_to_points):
  list_of_tups = list(players_to_points.items())
  list_of_tups.sort(key = lambda x: x[1], reverse = True)
  #sorts the list of tups according to the 2nd item of each tuple in descending order
  for i in range(len(list_of_tups)):
    print(f'{list_of_tups[i][0]} is Number {i+1} with {list_of_tups[i][1]} points')



#update_point_totals('no')
#print_ranks(players_to_points)

def play_game():
  #this function wont work on the codecademy terminal
  while True:
    x = input(guide)
    if x.upper() == 'A':
        player = input('What is the players name \n \t')
        word = input(f'what word was played by {player} \n \t') 
        play_word(player, word)
    elif x.upper() == 'B':
        update_point_totals()
    elif x.upper() == 'C':
        update_point_totals('no')
        print_ranks(players_to_points)
    elif x.upper() == 'D':
        print(list(zip(letters, points)))
    elif x.upper() == 'E':
        print(players_to_words)
    elif x.upper() == 'F':
        players_to_words.clear()
        players_to_points.clear()
    else:
        print('Invalid choice, try again \n')
    time.sleep(1)

play_game()