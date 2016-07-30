#!/bin/python

import logging, sys

my_bank = []
enemy_bank = []
turn = -1
draw_adv = []

def calculate_bid(player,pos,first_moves,second_moves):
    
    # helper function
    if player == 1:
        my_moves = first_moves
        enemy_moves = second_moves
    else:
        my_moves = second_moves
        enemy_moves = first_moves
    
    # update game state info
    global turn
    global first_bank
    global second_bank
    
    # turn is 0-indexed
    turn += 1
    
    # initial state
    if turn == 0:
        my_bank.append(100)
        enemy_bank.append(100)
        draw_adv.append[1]
    else:
        if my_moves[turn-1] 
    
    
    
    
    debugMsg = 'turn: ' + str(len(first_moves)) + '\n'
    debugMsg += str(first_moves) + '\n'
    
    """your logic here"""
    sys.stderr.write(debugMsg)
    
    return 5







#gets the id of the player
player = input()

scotch_pos = input()         #current position of the scotch

first_moves = [int(i) for i in raw_input().split()]
second_moves = [int(i) for i in raw_input().split()]
bid = calculate_bid(player,scotch_pos,first_moves,second_moves)
print bid
