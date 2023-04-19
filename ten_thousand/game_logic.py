
from random import randint
from collections import Counter


class GameLogic:

    def __init__(self) :
        pass


    def calculate_score(dice_roll):
        counter=Counter(dice_roll)
        score = 0

        '''
        Args:
            param1 : tuple of intger
        Returns:
            retun a number debend ten thousends game dice_roll as a score
    
        Raises:
          empty tuple
        '''
        
        for num in set(dice_roll):
            times=counter[num]
            if times >=3 :

                if num == 1 :
                    score +=1000
                if num == 2 :
                    score +=200
                if num == 3 :
                    score +=300
                if num == 4 :
                    score +=400
                if num == 5 :
                    score +=500
                if num == 6 :
                    score +=600

                if times ==4:
                    score *=2
                if times ==5:
                    score *=4   
                if times ==6:
                   score *=8 

        if counter[5] <3:
             score +=50 * counter[5]

        if counter[1] <3:
            score +=100 * counter[1]
        


        
        if all(count == 2 for count in counter.values()) and len(counter) == 3:
                    score =1500
        
        
        

        # if counter[1] and counter[2] and counter[3] and counter[4] and counter[5] and counter[6] ==1:   
        #         score = 1500

        
        ls=list(dice_roll)
        ls.sort()
        if ls == [1,2,3,4,5,6]:
            
             score = 1500

        return score
    
    
    def roll_dice(num):

        '''
        Args:
            param1 : number   from 1 = 6
        Returns:
            retun a number debend ten thousends game dice_roll as a score
    
        Raises:
          negative number and hieghr than 6
        '''
        if num >=1 and num <=6 :
            
            values=[]
            for x in range(num):
                x = randint(1, 6)
                values.append(x)
            
        return  tuple(values)
    

dice_roll=(5,)
print(GameLogic.calculate_score(dice_roll))