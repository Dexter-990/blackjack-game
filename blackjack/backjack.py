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
        elif updated_user_score < updated_comp_score:
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
    another_card = bool
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







