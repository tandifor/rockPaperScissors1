'''
Created on Sep 27, 2018

@author: ITAUser
'''
keepPlaying = True
while(keepPlaying):
#    '''Welcomes the player and tells the the rules'''
    print("Welcome to Rock Paper Scissors!")
    print("Best two out of three. Press 'q' to quit")
    
#    '''
#    1 = Rock
#    2 = Scissors
#    3 = Paper 
#    '''
    
#    '''imports the 'random' functon, which selects random values in a given range'''
    import random
        
#    '''sets each player's initial score to zero'''
    cpuScore = 0
    humanScore = 0
    
#    '''loop that repeats each round until the human or cpu score 2 points'''
    while(humanScore < 2 and cpuScore < 2):
        
#       '''assigns the variable 'cpuChoice' a random integer between 1 and 3'''
        cpuChoice = random.randint(1,3)
        
#        '''prompts the user to input their choice of rock, paper, or scissors'''
        choice = input("Please choose(Rock, Paper, Scissors): ")
        
#        '''checks is the user quits'''
        if( (choice == 'q') or (choice == 'Q') ):
            keepPlaying = False
            break
        
#        '''checks if it's a draw'''
        elif((choice.lower() == 'rock' and cpuChoice == 1)
            or (choice.lower() == 'scissors' and cpuChoice == 2) 
            or (choice.lower() == 'paper' and cpuChoice == 3)):
            print("DRAW")
            print ("Human:" + str(humanScore) , "CPU:" + str(cpuScore))
 
             
#         '''checks if human wins'''      
        elif((choice.lower() == 'rock' and cpuChoice == 2) 
            or (choice.lower() == 'scissors' and cpuChoice == 3) 
            or (choice.lower() == 'paper' and cpuChoice == 1)):
            humanScore = humanScore + 1
            print ("Human:" + str(humanScore) , "CPU:" + str(cpuScore))
  
#                       
#         '''checks if CPU wins'''
        elif((choice.lower() == 'rock' and cpuChoice == 3) 
            or (choice.lower() == 'scissors' and cpuChoice == 1) 
            or (choice.lower() == 'paper' and cpuChoice == 2)):
            cpuScore = cpuScore + 1
            print ("Human:" + str(humanScore) , "CPU:" + str(cpuScore))

        else: 
            print ("Not a valid input, try again.")
print ("Thanks for playing!")
if(humanScore == 2):
    print("You WIN!!!!")
if(cpuScore == 2):
    print("You LOSE!!!")
print ("Human:" + str(humanScore) , "CPU:" + str(cpuScore))