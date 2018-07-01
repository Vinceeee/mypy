#coding=utf-8
#! usr/bin/python
'''
Rochambeau , 即“石头-剪刀-布"
'''

# Import module below
import random

# Variable Declaration Area
WIN='W'
DRAW='D'
LOSE='L'

Game_Choice={"0":"Rock","1":"Scissor","2":"Paper"}

# 0 -- 石头 , 1 -- 剪刀 , 2 -- 布
Game_Rule={"00":DRAW,"01":WIN,"02":LOSE,
           "10":LOSE,"11":DRAW,"12":WIN,
           "20":WIN,"21":LOSE,"22":DRAW
           }

user_input=""
coputer_input=""

# Function Declaration Area
## check the result of the game:
def result_checking(i,u):
  str_i = str(i)
  str_u = str(u)
  print " *** your choice is %s        " % (Game_Choice[str_i])
  print " *** computer's choice is %s  " % (Game_Choice[str_u])
  result=str_i+str_u
  print result
  if Game_Rule[result] == WIN:
    print " You WINNNNNNNNNNNNNNNN ! "
  elif Game_Rule[result] == LOSE:
    print " You LOOOOOOOOOOOOOOOSE ! "
  elif Game_Rule[result] == DRAW:
    print " DRAW　GAME ! "

# Main Start Here

print "**************************************** Game Start !**********************************************"
print "*** 0 -- For Rock , 1 -- For Scissor , 2 -- For Paper  Q -- Exit"
user_input=raw_input("*** What you want to choose ? >> ")

while user_input != 'Q':
  if int(user_input) not in range(3):
    print "*** You are not obeying the Rule !!! OUTTTTTTTTT! "
    exit
  else:
    computer_input=random.randint(0,2)
    result_checking(user_input,computer_input)
  user_input=raw_input("*** Continue ? (Press Q to exit the game) >> ")

print "*** Game Over ... "
