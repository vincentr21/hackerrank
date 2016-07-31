#!/bin/python

import logging, sys

def calculate_bid(player,pos,first_moves,second_moves):
        
    # turn is 0-indexed
    turn = len(first_moves)
    
    # helper function
    if player == 1:
        my_moves = first_moves
        enemy_moves = second_moves
    else:
        my_moves = second_moves
        enemy_moves = first_moves
    
    # game state variables
    my_bank = []
    enemy_bank = []

    my_nominal = []
    enemy_nominal =[]

    my_steps_to_win = []
    enemy_steps_to_win = []

    draw_adv = []
    #================================= update game state variables ===============================================

    # first turn initial state
    my_bank.append(100)
    enemy_bank.append(100)

    my_nominal.append(10)
    enemy_nominal.append(10)

    my_steps_to_win.append(5)
    enemy_steps_to_win.append(5)

    draw_adv.append(1)
        
    # mid game states
    for T in range(1,turn+1):
        # case: same bid amount
        if my_moves[T-1] == enemy_moves[T-1]:
            if player == 1:
                if draw_adv[T-1] == 1:
                    my_bank.append(my_bank[T-1] - my_moves[T-1])
                    enemy_bank.append(enemy_bank[T-1])
                    my_steps_to_win.append(my_steps_to_win[T-1]-1)
                    enemy_steps_to_win.append(enemy_steps_to_win[T-1]+1)
                else:
                    my_bank.append(my_bank[T-1])
                    enemy_bank.append(enemy_bank[T-1] - enemy_moves[T-1])
                    my_steps_to_win.append(my_steps_to_win[T-1]+1)
                    enemy_steps_to_win.append(enemy_steps_to_win[T-1]-1)
            else: #player is 2
                if draw_adv[T-1] == 1:
                    my_bank.append(my_bank[T-1])
                    enemy_bank.append(enemy_bank[T-1] - enemy_moves[T-1])
                    my_steps_to_win.append(my_steps_to_win[T-1]+1)
                    enemy_steps_to_win.append(enemy_steps_to_win[T-1]-1)
                else:
                    my_bank.append(my_bank[T-1] - my_moves[T-1])
                    enemy_bank.append(enemy_bank[T-1])
                    my_steps_to_win.append(my_steps_to_win[T-1]-1)
                    enemy_steps_to_win.append(enemy_steps_to_win[T-1]+1)
            draw_adv.append(3-draw_adv[T-1])
        # case: my bid higher    
        elif my_moves[T-1] > enemy_moves[T-1]:
            my_bank.append(my_bank[T-1] - my_moves[T-1])
            enemy_bank.append(enemy_bank[T-1])
            my_steps_to_win.append(my_steps_to_win[T-1]-1)
            enemy_steps_to_win.append(enemy_steps_to_win[T-1]+1)
        # case: enemy bid higher
        else:
            my_bank.append(my_bank[T-1])
            enemy_bank.append(enemy_bank[T-1] - enemy_moves[T-1])
            my_steps_to_win.append(my_steps_to_win[T-1]+1)
            enemy_steps_to_win.append(enemy_steps_to_win[T-1]-1)

        
        my_nominal.append(my_bank[T]/(my_steps_to_win[T]*1))
        enemy_nominal.append(enemy_bank[T]/(enemy_steps_to_win[T]*1))
    
    
    # now for the strategies
    my_bid = my_nominal[turn]
    #my_bid = 10
    
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
