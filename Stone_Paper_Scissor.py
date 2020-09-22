#Stone,Paper and Scissor

import random
print("Let's play Stone,Paper and Scissors")
print("Remember,")
print("Stone beats Scissor")
print("Scissor beats Paper")
print("Paper beats Stone")

def User_Choice():
    print("Press 1 for Stone")
    print("Press 2 for Paper")
    print("Press 3 for Scissor")

Y=0
C=0

choice=True
while(choice):
    User_Choice()
    User_choice=int(input())
    if User_choice==1:
        print("I choose Stone")
        Computer_choice=random.randint(1,3)
        if  Computer_choice==1:
            print("Computer Response:-Stone")
            print("It's a Draw")
        elif Computer_choice==2:
            print("Computer Response:-Paper")
            print("You've lose this round")
        elif Computer_choice==3:
            print("Computer Response:-Scissor")
            print("Congrats!! You win this round")
        
    elif User_choice==2:
        print("I choose Paper")
        Computer_choice=random.randint(1,3)
        if  Computer_choice==1:
            print("Computer Response:-Stone")
            print("Congrats!! You win this round")
        elif Computer_choice==2:
            print("Computer Response:-Paper")
            print("It's a Draw")
        elif Computer_choice==3:
            print("Computer Response:-Scissor")
            print("You've lose this round")
            
    elif User_choice==3:
        print("I choose Scissor")
        Computer_choice=random.randint(1,3)
        if  Computer_choice==1:
            print("Computer Response:-Stone")
            print("You've lose this round")
        elif Computer_choice==2:
            print("Computer Response:-Paper")
            print("Congrats!! You win this round")
        elif Computer_choice==3:
            print("Computer Response:-Scissor")
            print("It's a Draw")
            
    else:
        print("Enter the valid choice and try again!")
        continue

    print("---Score---")
    
    if User_choice==1 and Computer_choice==1:
        temp1=0
        temp2=0
    if User_choice==1 and Computer_choice==2:
        temp1=0
        temp2=1
    if User_choice==1 and Computer_choice==3:
        temp1=1
        temp2=0

    if User_choice==2 and Computer_choice==1:
        temp1=1
        temp2=0
    if User_choice==2 and Computer_choice==2:
        temp1=0
        temp2=0
    if User_choice==2 and Computer_choice==3:
        temp1=0
        temp2=1

    if User_choice==3 and Computer_choice==1:
        temp1=0
        temp2=1
    if User_choice==3 and Computer_choice==2:
        temp1=1
        temp2=0
    if User_choice==3 and Computer_choice==3:
        temp1=0
        temp2=0

    
    Y=Y+temp1
    C=C+temp2
    print("You:",Y)
    print("Computer:",C)
    print("--------------------")
    
    if Y==5 or C==5:
            break


if Y==5:
    print("Congrats you're the final winner you beat the computer with a total score of ",Y,"-",C,)
if C==5:
    print("You lose by total score of ",C,"-",Y)

print("Thank-You for playing")
