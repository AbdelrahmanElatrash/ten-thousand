
# import sys
# import os
# path1=  os.path.abspath(os.getcwd())+'/ten_thousand'
# sys.path.insert(1,os.getcwd()+'/ten_thousand')

try:
    from game_logic import GameLogic 
except:
    from ten_thousand.game_logic import GameLogic





roll_dice=GameLogic.roll_dice   # roll dice function to generate random number

def play(roller=GameLogic.roll_dice, num=10):

    """
    do:  this function start the game and do game stepse
    arg : 2 parm 
        roller : roll dise function
        num : number of round to play
    return :
        total score of the game 
    """
    
    global roll_dice
    roll_dice= roller

    user_choice=invite()   # invet function ask user to lay or not

    if user_choice=="y":
        start_game(num)   # do game steps and play
    else:
        print('OK. Maybe another time')



def invite():
    """
    welcoming messege to start play 
    user choice y to play or n to decline
    """
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')

    user_choice=input("> ")

    return user_choice.lower()


def start_game(num_round):

    """
    do: start game and calculate score 
    args : 
        num_round : int number of rounds that user can play come from play function
    return :
        score point as a int number
    """
    round_num=1
    score=0

    while round_num <= num_round:
        round_result= roll_and_calculate(round_num)     # do roll and calculate score from game logic

        if round_result == -1:
            break
        print(f'You banked {round_result} points in round {round_num}')
        score +=round_result                               # add unbanked point that come from roll_and_calculate(round_num) to the total score
        print(f'Total score is {score} points')
        round_num +=1
    print(f'Thanks for playing. You earned {score} points')
    



def roll_and_calculate(round_num):

    """
    do : start roll dice and calculate score
    args :
        round_num: int the round number come from start game function
    return :
        the point collected from each round as unbanked_point for added  to score
    """
    avilable_dice=6
    unbanked_point=0
    print(f'Starting round {round_num}')

    while not(avilable_dice==0):

        print(f'Rolling {avilable_dice} dice...')

        roll=roll_dice(avilable_dice)
        
        printed_roll_value=format_roll(roll)
        print(printed_roll_value)

        if GameLogic.calculate_score(roll)==0:
            zlich()
            return 0

        
        keeps_dice=choise_point(roll)
        keeps_dice=GameLogic.get_scorers(keeps_dice)
        if  len(keeps_dice)==0:
            return -1
        elif len(keeps_dice)==6:
            unbanked_point +=GameLogic.calculate_score(keeps_dice)
        else:
            unbanked_point +=GameLogic.calculate_score(keeps_dice)
            avilable_dice -=len(keeps_dice)
        

  
        print(f'You have {unbanked_point} unbanked points and {avilable_dice} dice remaining')    
        print('(r)oll again, (b)ank your points or (q)uit:')
        roll_bank_or_quite=input('> ')
        if roll_bank_or_quite.lower()== 'q':
            return -1
        elif roll_bank_or_quite== 'b':
            return unbanked_point
        elif avilable_dice==0:
            return 0

def zlich():
    print('****************************************')
    print('**        Zilch!!! Round over         **')
    print('****************************************')

def choise_point(roll):

    """
    do: take roll result and let user choise the number to calculate score
    args :
        roll : tuple of int that come from dice roll function
    return :
        keeps_dice  : tuples of choisen number 
    """
    print('Enter dice to keep, or (q)uit:')
    keep_or_quite=input('> ')
    
    if keep_or_quite.lower()=='q':
        return tuple()
    
    keeps_dice=convert_keep_to_int(keep_or_quite)
    valid=GameLogic.validate_keepers(roll,keeps_dice)

    if valid:
        return keeps_dice 
    else:
        print('Cheater!!! Or possibly made a typo...')
        format=format_roll(roll)
        print(format)
        return choise_point(roll)

            
        




def format_roll(roll): # for test
    """
    do : convert touble that come from roll dice to streng for test
    args:
        roll :touble that come from roll dice
    return :
        str like this *** 1 5 2 4 2 5 ***
    """
    values_as_str=[str(value) for value in roll]
    formated_roll=" ".join(values_as_str)
    return f'*** {formated_roll} ***'

    

def convert_keep_to_int(keep_or_quite):
    """
    do : convert str of numbers that user input to int and setthem in tuple
    parm : str input from user 
    return : convert user input to int and return tuple of int
    """
    values=[int(value) for value in keep_or_quite if value.isdigit()]
    return tuple(values)




if __name__=="__main__":
    play()
    