############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
from art import logo
cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



print(logo)

computer_choice = ["yes", "no"]

def user_f_ace(fc):
    if fc == "Ace":
        which_ace = input("You picked ace for your first card, do you want '11' or '1'?")
        if which_ace == "11":
            fc = 11
            return fc
        elif which_ace == '1':
            fc = 1
            return fc
    else:
        return fc
def user_s_ace(sc):
    if sc == "Ace":
        which_ace = input("You picked ace for your second card, do you want '11' or '1'?")
        if which_ace == '11':
            sc = 11
            return sc
        elif which_ace == '1':
            sc = 1
            return sc
    else:
        return sc
def user_t_ace(tc):
    if tc == "Ace":
        which_ace = input("You picked ace, do you want '11' or '1'?")
        if which_ace == '11':
            tc = 11
            return tc
        elif which_ace == '1':
            tc = 1
            return tc
    else:
        return tc
def comp_f_ace(fc):
    ace = ["11", "1"]
    if fc == "Ace":
        which_ace = random.choice(ace)
        if which_ace == '11':
            fc = 11
            return fc
        elif which_ace == '1':
            fc = 1
            return fc
    else:
        return fc
def comp_s_ace(sc):
    ace = ["11", "1"]
    if sc == "Ace":
        which_ace = random.choice(ace)
        if which_ace == '11':
          sc = 11
          return sc
        elif which_ace == '1':
          sc = 1
          return sc
    else:
        return sc
def comp_t_ace(tc):
    ace = ["11", "1"]
    if tc == "Ace":
        which_ace = random.choice(ace)
        if which_ace == '11':
            tc = 11
            return tc
        elif which_ace == '1':
            tc = 1
            return tc
    else:
        return tc
def computers_choice(choice):
    random.choice(choice)

def update_users_cards(card_info):
    
    updated_card = info["users_info"]["cards"].append(card_info)
    return updated_card   

def update_comp_cards(card_info):
    info["computer_info"]["cards"].append(card_info)
    return info["computer_info"]["cards"].append(card_info)

def update_users_score(score, card):
    user_t_ace(card)
    users_score = add_users_score(score, card)  
    info["users_info"]["score"] = users_score
    updated_user_score = info["users_info"]["score"]
    
def update_comp_score(score, card):
    computers_score = info["computers_info"]["score"]
    info["computers_info"]["score"] = add_computers_score(computers_score, card)
    updated_comp_score = info["computers_info"]["score"]
    

def add_users_score(n1, n2):
    return n1 + n2

def add_computers_score(n1, n2):
    return n1 + n2
def final_hand():
        updated_user_score = info["users_info"]["score"]
        updated_comp_score = info["computers_info"]["score"]
        if updated_user_score == 21:
            print(f"You won before the game got interesting\n Your cards are {users_cards}, your score is {users_score}\n Computers score is {computers_score}\nComputer's cards are {computers_cards}")
            another_card = False
        elif updated_comp_score == 21:
            print(f"You lose\n Your cards are {users_cards}, your score is {users_score}\n Computers score is {computers_score}\nComputer's cards are {computers_cards}.  ")
            
        elif updated_user_score > updated_comp_score:
            print(f"You win\n Your cards are {users_cards}, your score is {users_score}\n Computers score is {computers_score}\nComputer's cards are {computers_cards}")
            another_card = False
        elif updated_user_score < update_comp_score:
            print(f"You lose\n Your cards are {users_cards}, your score is {users_score}\n Computers score is {computers_score}\nComputer's cards are {computers_cards}.  ")
            another_card = False
        go_again = input("Do you want to restart. Type 'yes' or 'no'")
        if go_again == "yes":
            start = True
        elif go_again == "no":
            another_card = False
            start = False
            print("Thank you for playing")    

def comps_go_again():
    if computers_choice(computer_choice) == "yes":
        com_t_card = random.choice(card)
        update_comp_score(computers_score, comp_t_ace(com_t_card))
        update_comp_cards(com_t_card)
    elif computers_choice(computer_choice) == "no":
        if another_card == "n":
            final_hand()
           
    






start1 = input("Do you want to play the game of blackjack?. Type 'yes' or 'no'\n").lower()

users_first_card = random.choice(cards)
users_second_card = random.choice(cards)
users_score = add_users_score(user_f_ace(users_first_card), user_s_ace(users_second_card))
info = {
    "users_info": {"score": users_score, 
    "cards": [users_first_card, users_second_card]},
    "computers_info": {"score": {},
    "cards": []}
        }
users_card = info["users_info"]["cards"]
users_score = info["users_info"]["score"] 
computers_f_card = random.choice(cards)
computers_s_card = random.choice(cards)
info["computers_info"]["cards"].extend([computers_f_card, computers_s_card])

info["computers_info"]["score"] = add_computers_score(comp_f_ace(computers_f_card), comp_s_ace(computers_s_card))

computers_score = info["computers_info"]["score"]
computers_cards = info["computers_info"]["cards"]


start =  True
if start1 != "yes":
    if start1 != "no":
        ask_again = True
        while ask_again:
            ask_again = input("You inputted an invalid option. Type 'yes'or'no'\n")
            if ask_again == "yes":
                ask_again = False
                start =  True
            elif ask_again == "no":
                ask_again = False
                start =  False
                print("You could have attempted at least")

if start1 == "no":
    print("You could have attempted at least")
    start = False



while start:
    print(f"Your card: {users_card}, Your score: {users_score}")
    
    print(f"Computer's first card: {computers_f_card}")
        
        
        # com_current_score = add_computers_score(computers_f_card, computers_s_card)
    users_score = info["users_info"]["score"]
    users_cards = info["users_info"]["cards"]
    if users_score == 21:
        print(f"You won before the game got interesting\n Your cards are {users_cards}, your score is {users_score}\n Computers score is {computers_score}\nComputer's cards are {computers_cards}")
        start = False
    elif computers_score == 21:
        print(f"You lost before the game got interesting\n Your cards are {users_cards}, your score is {users_score}\n Computers score is {computers_score}\nComputer's cards are {computers_cards}.  ")
        start = False
            
    another_card_1 = input("Type 'y' to get another card or 'n' to pass\n")
    if another_card_1 == "y":
        another_card = True
    elif another_card_1 == "n":
        final_hand()
    while another_card:
        users_score = info["users_info"]["score"]
        users_t_card = random.choice(cards)
        user_t_ace(users_t_card)
        update_users_score(users_score, user_t_ace(users_t_card))
        update_users_cards(users_t_card)
         
        updated_user_score = info["users_info"]["score"]
        updated_comp_score = info["computers_info"]["score"]
        another_card = False
    
        #computer's decision to pick another and what would happen after that begins from here
    comps_go_again()







