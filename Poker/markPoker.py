#!/usr/bin/env python
#import funcs files
import sys
from pokerFuncs import *

best_hand = {}
    #highest - the highest card in hand
    #hand - the card nums in array saved in case of high card tie
    #best - the best hand saved as an int to compare to other players:
            #5 - straight flush
            #4 - 3 of a kind
            #3 - straight
            #2 - flush
            #1 - pair
            #0 - high card
    #high_pair - the num of the pair for tie purposes
    #high_triple - the num of the triple for tie purposes
    #id - the id of the player
currentBestHand = []
#input to pragram is STDIN
num_players = input()
for player in range(int(num_players)):
    player_hand = {}
    line = raw_input()
    line = line.split(' ')
    current_hand = findBestHand(line)
    #returns dictionary with data filled in

    if len(currentBestHand) == 0:
        currentBestHand.append(current_hand) 

    else:
        if currentBestHand[0]['best'] < current_hand['best']:
            currentBestHand = [current_hand]
        elif currentBestHand[0]['best'] == current_hand['best']:
            currentBestHand = tieComparisons(currentBestHand, current_hand)

ids = ''
for i in currentBestHand:
    ids += str(i['id']) + ' '    
    #this is originally had it to print each id with end='', 
    #but the executeable didn't like that
print(ids)
