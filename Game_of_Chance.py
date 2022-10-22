import random 

def roll_dice():
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return(die1,die2)

def display_dice(dice):
    die1,die2 = dice
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')
prev_dice = 0
new_dice = 0
while(1):
    r = input("Enter R to roll (Q to exit): ")
    if r== "R":
        count = 0 
        dice=roll_dice()
        sum_of_dice = sum(dice)
        prev_dice = new_dice
        new_dice = sum_of_dice
        
        if(count == 0 and sum_of_dice==7 or sum_of_dice == 11):
            display_dice(dice)
            print("You Win")
            break
        elif (count == 0 and sum_of_dice == 2 or sum_of_dice == 3 or sum_of_dice == 12):
            display_dice(dice)
            print("You win nothing, you looose, good day sir!")
            break
        else:
            display_dice(dice)
            print("Your point is " + str(sum_of_dice))
            
            if(new_dice == prev_dice):
                print("You Win !!!")
                break
        count= count + 1    
    elif r == "Q":
        break       
        