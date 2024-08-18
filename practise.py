import math
import sys
import time
import random
from time import sleep

global enemy_name
enemy_health = int(0)
enemy_stun = int(0)
enemy_attack_1 = int(0)
enemy_attack_1_name = "nil"
enemy_attack_2 = int(0)
global enemy_attack_2_name
enemy_attack_3 = int(0)
enemy_attack_3_name = "nil"
enemy_attack_used = enemy_attack_1
enemy_hit_chance = 0
player_level = int(0)
manna_meter = 5 + player_level
player_health = 10 + player_level
attack_hit_chance = 0
damage_dealt = 0


moves = [
    [0,1,2,3,4],
    ["name","move1","move2","move3","move4"],
    ["cost",0,0,0,0],
    ["attack",0,0,0,0],
    ["healing",0,0,0,0],
    ["defense",0,0,0,0],
    ["stun",0,0,0,0]
    ]
# def moves_equiping():
#a tier attack(4,6,0,0,2)
def equip_fireball(move_slot):
    if move_slot==1:
        moves[1][1] = "fireball"
        moves[2][1] = 4
        moves[3][1] = 6
        moves[4][1] = 0
        moves[5][1] = 0
        moves[6][1] = 2
    if move_slot==2:
        moves[1][2] = "fireball"
        moves[2][2] = 4
        moves[3][2] = 6
        moves[4][2] = 0
        moves[5][2] = 0
        moves[6][2] = 2
    if move_slot==3:
        moves[1][3] = "fireball"
        moves[2][3] = 4
        moves[3][3] = 6
        moves[4][3] = 0
        moves[5][3] = 0
        moves[6][3] = 2
    if move_slot==4:
        moves[1][4] = "fireball"
        moves[2][4] = 4
        moves[3][4] = 6
        moves[4][4] = 0
        moves[5][4] = 0     
        moves[6][4] = 2       

#c tier attack(2,3,0,0,1)
def equip_arrows(move_slot):
    if move_slot==1:
        moves[1][1] = "arrows"
        moves[2][1] = 2
        moves[3][1] = 3
        moves[4][1] = 0
        moves[5][1] = 0
        moves[6][1] = 1
    if move_slot==2:
        moves[1][2] = "arrows"
        moves[2][2] = 2
        moves[3][2] = 3
        moves[4][2] = 0
        moves[5][2] = 0
        moves[6][2] = 1
    if move_slot==3:
        moves[1][3] = "arrows"
        moves[2][3] = 2
        moves[3][3] = 3
        moves[4][3] = 0
        moves[5][3] = 0
        moves[6][3] = 1
    if move_slot==4:
        moves[1][4] = "arrows"
        moves[2][4] = 2
        moves[3][4] = 3
        moves[4][4] = 0
        moves[5][4] = 0
        moves[6][4] = 1 

#b tier attack(3,0,1,5,0)      
def equip_block(move_slot):
    if move_slot==1:
        moves[1][1] = "block"
        moves[2][1] = 3
        moves[3][1] = 0
        moves[4][1] = 1
        moves[5][1] = 5
        moves[6][1] = 0
    if move_slot==2:
        moves[1][2] ="block"
        moves[2][2] = 3
        moves[3][2] = 0
        moves[4][2] = 1
        moves[5][2] = 5
        moves[6][2] = 0  
    if move_slot==3:
        moves[1][3] ="block"
        moves[2][3] = 3
        moves[3][3] = 0
        moves[4][3] = 1
        moves[5][3] = 5
        moves[6][3] = 0
    if move_slot==4:
        moves[1][4] = "block"
        moves[2][4] = 3
        moves[3][4] = 0
        moves[4][4] = 1
        moves[5][4] = 5
        moves[6][4] = 0

#d tier attack(1,0,2,0,0)      
def equip_sleep(move_slot):
    if move_slot==1:
        moves[1][1] = "sleep"
        moves[2][1] = 1
        moves[3][1] = 0
        moves[4][1] = 2
        moves[5][1] = 0
        moves[6][1] = 0
    if move_slot==2:
        moves[1][2] = "sleep"
        moves[2][2] = 1
        moves[3][2] = 0
        moves[4][2] = 2
        moves[5][2] = 0
        moves[6][2] = 0  
    if move_slot==3:
        moves[1][3] = "sleep"
        moves[2][3] = 1
        moves[3][3] = 0
        moves[4][3] = 2
        moves[5][3] = 0
        moves[6][3] = 0
    if move_slot==4:
        moves[1][4] = "sleep"
        moves[2][4] = 1
        moves[3][4] = 0
        moves[4][4] = 2
        moves[5][4] = 0
        moves[6][4] = 0

#b tier attack(3,0,5,1,0)
def equip_heal(move_slot):
    if move_slot==1:
        moves[1][1] = "heal"
        moves[2][1] = 3
        moves[3][1] = 0
        moves[4][1] = 5
        moves[5][1] = 1
        moves[6][1] = 0
    if move_slot==2:
        moves[1][2] = "heal"
        moves[2][2] = 3
        moves[3][2] = 0
        moves[4][2] = 5
        moves[5][2] = 1
        moves[6][2] = 0  
    if move_slot==3:
        moves[1][3] = "heal"
        moves[2][3] = 3
        moves[3][3] = 0
        moves[4][3] = 5
        moves[5][3] = 1
        moves[6][3] = 0
    if move_slot==4:
        moves[1][4] = "heal"
        moves[2][4] = 3
        moves[3][4] = 0
        moves[4][4] = 5
        moves[5][4] = 1
        moves[6][4] = 0  

#d tier attack(1,2,0,0,0)
def equip_punch(move_slot):
    if move_slot==1:
        moves[1][1] = "punch"
        moves[2][1] = 1
        moves[3][1] = 2
        moves[4][1] = 0
        moves[5][1] = 0
        moves[6][1] = 0
    if move_slot==2:
        moves[1][2] = "punch"
        moves[2][2] = 1
        moves[3][2] = 2
        moves[4][2] = 0
        moves[5][2] = 0
        moves[6][2] = 0
    if move_slot==3:
        moves[1][3] = "punch"
        moves[2][3] = 1
        moves[3][3] = 2
        moves[4][3] = 0
        moves[5][3] = 0
        moves[6][3] = 0
    if move_slot==4:
        moves[1][4] = "punch"
        moves[2][4] = 1
        moves[3][4] = 2
        moves[4][4] = 0
        moves[5][4] = 0
        moves[6][4] = 0

#b tier attack(3,3,0,1,2)
def equip_axe_strike(move_slot):
    if move_slot==1:
        moves[1][1] = "axe strike"
        moves[2][1] = 3
        moves[3][1] = 3
        moves[4][1] = 0
        moves[5][1] = 1
        moves[6][1] = 2
    if move_slot==2:
        moves[1][2] = "axe strike"
        moves[2][2] = 3
        moves[3][2] = 3
        moves[4][2] = 0
        moves[5][2] = 1
        moves[6][2] = 2
    if move_slot==3:
        moves[1][3] = "axe strike"
        moves[2][3] = 3
        moves[3][3] = 3
        moves[4][3] = 0
        moves[5][3] = 1
        moves[6][3] = 2
    if move_slot==4:
        moves[1][4] = "axe strike"
        moves[2][4] = 3
        moves[3][4] = 3
        moves[4][4] = 0
        moves[5][4] = 1
        moves[6][4] = 2

#a tier attack(4,4,0,4,0)
def equip_sword_strike(move_slot):
    if move_slot==1:
        moves[1][1] = "sword strike"
        moves[2][1] = 4
        moves[3][1] = 4
        moves[4][1] = 0
        moves[5][1] = 4
        moves[6][1] = 0
    if move_slot==2:
        moves[1][2] = "sword strike"
        moves[2][2] = 4
        moves[3][2] = 4
        moves[4][2] = 0
        moves[5][2] = 4
        moves[6][2] = 0  
    if move_slot==3:
        moves[1][3] = "sword strike"
        moves[2][3] = 4
        moves[3][3] = 4
        moves[4][3] = 0
        moves[5][3] = 4
        moves[6][3] = 0
    if move_slot==4:
        moves[1][4] = "sword strike"
        moves[2][4] = 4
        moves[3][4] = 4
        moves[4][4] = 0
        moves[5][4] = 0
        moves[6][4] = 4  

#b tier attack(4,2,0,0,6)
def equip_freeze(move_slot):
    if move_slot==1:
        moves[1][1] = "freeze"
        moves[2][1] = 4
        moves[3][1] = 2
        moves[4][1] = 0
        moves[5][1] = 0
        moves[6][1] = 6
    if move_slot==2:
        moves[1][2] = "freeze"
        moves[2][2] = 4
        moves[3][2] = 2
        moves[4][2] = 0
        moves[5][2] = 0
        moves[6][2] = 6  
    if move_slot==3:
        moves[1][3] = "freeze"
        moves[2][3] = 4
        moves[3][3] = 2
        moves[4][3] = 0
        moves[5][3] = 0
        moves[6][3] = 6
    if move_slot==4:
        moves[1][4] = "freeze"
        moves[2][4] = 4
        moves[3][4] = 2
        moves[4][4] = 0
        moves[5][4] = 0
        moves[6][4] = 6  

#s tier attack(5,0,5,0,5)
def equip_suck_manna(move_slot):
    if move_slot==1:
        moves[1][1] = "suck manna"
        moves[2][1] = 5
        moves[3][1] = 0
        moves[4][1] = 5
        moves[5][1] = 0
        moves[6][1] = 5
    if move_slot==2:
        moves[1][2] = "suck manna"
        moves[2][2] = 5
        moves[3][2] = 0
        moves[4][2] = 5
        moves[5][2] = 0
        moves[6][2] = 5
    if move_slot==3:
        moves[1][3] = "suck manna"
        moves[2][3] = 5
        moves[3][3] = 0
        moves[4][3] = 5
        moves[5][3] = 0
        moves[6][3] = 5
    if move_slot==4:
        moves[1][4] = "suck manna"
        moves[2][4] = 5
        moves[3][4] = 0
        moves[4][4] = 5
        moves[5][4] = 0
        moves[6][4] = 5

#s tier attack(7,10,0,2,2)
def equip_double_sword_attack(move_slot):
    if move_slot==1:
        moves[1][1] = "double sword attack"
        moves[2][1] = 7
        moves[3][1] = 10
        moves[4][1] = 0
        moves[5][1] = 2
        moves[6][1] = 2
    if move_slot==2:
        moves[1][2] = "double sword strike"
        moves[2][2] = 7
        moves[3][2] = 10
        moves[4][2] = 0
        moves[5][2] = 2
        moves[6][2] = 2  
    if move_slot==3:
        moves[1][3] = "double sword strike"
        moves[2][3] = 7
        moves[3][3] = 10
        moves[4][3] = 0
        moves[5][3] = 2
        moves[6][3] = 2
    if move_slot==4:
        moves[1][4] = "double sword strike"
        moves[2][4] = 7
        moves[3][4] = 10
        moves[4][4] = 0
        moves[5][4] = 2
        moves[6][4] = 2

#s tier return(6,0,0,∞,0)      
def equip_return(move_slot):
    if move_slot==1:
        moves[1][1] = "return"
        moves[2][1] = 6
        moves[3][1] = enemy_attack_used
        moves[4][1] = 0
        moves[5][1] = 10000
        moves[6][1] = 0
    if move_slot==2:
        moves[1][2] ="return"
        moves[2][2] = 6
        moves[3][2] = enemy_attack_used
        moves[4][2] = 0
        moves[5][2] = 10000
        moves[6][2] = 0  
    if move_slot==3:
        moves[1][3] ="return"
        moves[2][3] = 6
        moves[3][3] = enemy_attack_used
        moves[4][3] = 0
        moves[5][3] = 10000
        moves[6][3] = 0
    if move_slot==4:
        moves[1][4] = "return"
        moves[2][4] = 6
        moves[3][4] = enemy_attack_used
        moves[4][4] = 0
        moves[5][4] = 10000
        moves[6][4] = 0

#ss tier blood_sacrifice(9,20,-2,0,0)      
def equip_blood_sacrifice(move_slot):
    if move_slot==1:
        moves[1][1] = "blood sacrifice"
        moves[2][1] = 9
        moves[3][1] = 20
        moves[4][1] = -2
        moves[5][1] = 0
        moves[6][1] = 0
    if move_slot==2:
        moves[1][2] ="blood sacrifice"
        moves[2][2] = 8
        moves[3][2] = 16
        moves[4][2] = 0
        moves[5][2] = 0
        moves[6][2] = 0  
    if move_slot==3:
        moves[1][3] ="blood sacrifice"
        moves[2][3] = 8
        moves[3][3] = 16
        moves[4][3] = 0
        moves[5][3] = 0
        moves[6][3] = 0
    if move_slot==4:
        moves[1][4] = "return"
        moves[2][4] = 8
        moves[3][4] = 16
        moves[4][4] = 0
        moves[5][4] = 0
        moves[6][4] = 0
equip_fireball(2)
print(moves)