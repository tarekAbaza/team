
from random import choice

#create a list of players from a file
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('Players:', players)

#create a list of team names from a file
teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print('Team names:', teamNames)

#create empty team lists
teamA = []
teamB = []
teamC = []

#loop until there are no players left
while len(players) > 0:
  
  #choose a random player for team A
  playerA = choice(players)
  teamA.append(playerA)
  #remove the player from the players list
  players.remove(playerA)
  
  #break out of the loop if there are no players left
  

  if players == []: 
    break
  
  #choose a random player for team B
  playerB = choice(players)
  teamB.append(playerB)
  #remove the player from the players list
  players.remove(playerB)
  if players == []: 
    break
  
  #choose a random player for team C
  playerC = choice(players)
  teamC.append(playerC)
  #remove the player from the players list
  players.remove(playerC)

#choose random team names for the 3 teams
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)
teamNameC = choice(teamNames)
teamNames.remove(teamNameC)

#print the teams
print('\nHere are your teams:\n')
print(teamNameA, teamA)
print(teamNameB, teamB)
print(teamNameC, teamC)