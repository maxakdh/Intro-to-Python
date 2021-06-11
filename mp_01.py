import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print ("Error: Not one of the 5 choices")


def number_to_name(number): 
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizards"
    elif number == 4:
        return "scissors"
    else:
        print ("Error: Number not in range.")


    
def rpsls(player_choice): 
    print (" ")
    player_number = name_to_number(player_choice)
    print ("Player Chooses: " + player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print ("Computer Chooses: "+ comp_choice)
    result = (comp_number - player_number) % 5

    if result >=1 and result <=2:
        print ("Computer Wins")
    elif result >=3 and result <=4:
        print ("Player Wins")
    else:
        print ("Player and computer tie!")
  
  

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


