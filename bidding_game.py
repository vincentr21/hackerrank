#!/bin/python

import logging, sys

# start of turn game state variables

my_bank = []
enemy_bank = []

my_nominal = []
enemy_nominal =[]

my_steps_to_win = []
enemy_steps_to_win = []

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
    
    # game state variables
    global turn
    global my_bank
    global enemy_bank
    global my_nominal
    global enemy_nominal
    global my_steps_to_win
    global enemy_steps_to_win 
    global turn
    
    #================================= update game state variables ===============================================
    
    # turn is 0-indexed
    turn = turn + 1
    my_bank.append(123)
    
    # first turn initial state
    if turn == 0:
        my_bank.append(100)
        enemy_bank.append(100)
        
        my_nominal.append(10)
        enemy_nominal.append(10)
        
        my_steps_to_win.append(5)
        enemy_steps_to_win.append(5)
        
        draw_adv.append(1)
        
    # mid game states
    else:
        # case: same bid amount
        if my_moves[turn-1] == enemy_moves[turn-1]:
            if player == 1:
                if draw_adv[turn-1] == 1:
                    my_bank.append(my_bank[turn-1] - my_move[turn-1])
                else:
                    enemy_bank.append(enemy_bank[turn-1] - enemy_move[turn-1])
            else: #player is 2
                if draw_adv[turn-1] == 1:
                    enemy_bank.append(enemy_bank[turn-1] - enemy_move[turn-1])
                else:
                    my_bank.append(my_bank[turn-1] - my_move[turn-1])
            draw_adv.append(3-draw_adv[turn-1])
        # case: my bid higher    
        elif my_moves[turn-1] > enemy_moves[turn-1]:
            my_bank.append(my_bank[turn-1] - my_move[turn-1])
        # case: enemy bid higher
        else:
            enemy_bank.append(enemy_bank[turn-1] - enemy_move[turn-1])
            
        my_steps_to_win.append(pos)
        enemy_steps_to_win.append(10-pos)
        
        my_nominal.append(my_bank[turn]/(my_steps_to_win[turn]*2))
        enemy_nominal.append(enemy_bank[turn]/(enemy_steps_to_win[turn]*2))
    
    # now for the strategies
    my_bid = my_nominal[turn]
    
    debugMsg = 'turn: ' + str(turn) + '\n'
    debugMsg += 'my moves: ' + str(my_moves) + '\n'
    debugMsg += 'enemy moves: ' + str(enemy_moves) + '\n'
    debugMsg += 'my bank: ' + str(my_bank) + '\n'
    debugMsg += 'enemy bank: ' + str(enemy_bank) + '\n'
    debugMsg += 'my nominal: ' + str(my_nominal) + '\n'
    debugMsg += 'enemy nominal: ' + str(enemy_nominal) + '\n'
    
    sys.stderr.write(debugMsg)
    
    return my_bid







#gets the id of the player
player = input()

scotch_pos = input()         #current position of the scotch

first_moves = [int(i) for i in raw_input().split()]
second_moves = [int(i) for i in raw_input().split()]
bid = calculate_bid(player,scotch_pos,first_moves,second_moves)
print bid
