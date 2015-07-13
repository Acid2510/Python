from random import randint

def enemy():
    rand=randint(1,3)
    if rand==1:
        return 'rock'
    elif rand==2:
        return 'paper'
    elif rand==3:
        return 'scissors'

def suit(player,enemy):
    if player==enemy:
        return 'draw'
    if player=="scissors":
        if enemy == "paper":
            return'you win'
        elif enemy == "rock":
            return'you lose'
    elif  player=="rock":
        if enemy == "scissors":
            return'you win'
        elif enemy == "paper":
            return'you lose'
    elif  player=="paper":
         if enemy == "rock":
             return'you win'
         elif enemy == "scissors":
            return'you lose'
        
def main_program():
    player=raw_input("what do you pick(Rock/Paper/scissors):")
    print suit(player,enemy())

main_program()
