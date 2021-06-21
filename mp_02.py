
import simplegui
import random
import math

counter = 10
num_range = 1000

# helper function to start and restart the game
def new_game():
    global secret_number, counter
    secret_number = random.randrange(0,num_range)   
    
    if num_range == 100:
        counter = 7
    elif num_range == 1000:
        counter = 10
       
   
    print 
    print ("New game. range is from 0 to" + str(num_range))
    print ("Number of remaining guess is" + str(counter))


# define event handlers for control panel
def range100():
   global num_range
   num_range = 100
   new_game()

def range1000():
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global counter 
    guessnum = int(guess)       
    print     
    print ("Guess was", guessnum)
    
    if num_range == 1000:
        if (guessnum >= 1000 or guessnum < 0):
            print ("Invalid Guess Number! Number Range Should Be [0, 1000).")
            
        if counter > 0:
            counter -= 1
            print ("Number of remaining guess is", counter)  
      
            if guessnum < secret_number:
                print ("Higher!")
            elif guessnum > secret_number:
                print ("Lower!")
            else:
                print ("Correct!")
                new_game()
        else:
            print
            print ("You ran out of guess. Guess was", secret_number)
            new_game()
    

    elif num_range == 100:
        if (guessnum >= 100 or guessnum < 0):
            print ("Invalid Guess Number! Number Range Should Be [0, 100).")
            
        if counter > 0: 
            counter -= 1
            print ("Number of remaining guess is", counter)  

            if guessnum < secret_number:
                print ("Higher!")
            elif guessnum > secret_number:
                print ("Lower!")
            else:
                print ("Correct!")
                new_game()            
        else:
            print ("You ran out of guess. Guess was", secret_number)
            new_game()

    
f = simplegui.create_frame ("Guess the number!", 300, 300)


f.add_button ("New Game", new_game, 100)
f.add_button ("Range 0 to 100", range100, 100)
f.add_button ("Range 0 to 1000", range1000, 100)
f.add_input ("Enter guess", input_guess, 100)


f.start()


new_game()


