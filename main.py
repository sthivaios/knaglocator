# Game imports choice from "random" library.
from random import choice

# Set score to 0 by default.
score=0

# Welcome the player.
print("Welcome!")

# Ask for their name.
username=input("What is your name?     >")


# Loop for 5 times (so 5 game rounds).
for x in range(0, 5):
    
    
    # Pick random L or R (left or right).
    answer=choice(["L", "R"])

    # Ask player where they think that Knag is located.
    useranswer=input("Ok " + username + "," + " where do you think Knag is?" + " (For left type L and for right R)     >")
    
    # Ignore case.
    if useranswer=="r":
        useranswer="R"
    elif useranswer=="l":
        useranswer="L"

    # Set variable humantype so game tells player that they picked the correct option that was "left" and not "l".
    # Essentially lines 32 to 35 converts L and R to human words.
    if answer=="L" or "l":
        humantype="left"
    elif answer=="R" or "r":
        humantype="right"

    # If answer player provided was right, score is increased by 1, and the player is informed.
    if answer==useranswer:
        score = score + 1
        print("Congratulations! You picked " + humantype + " which was the right answer!")
    
    # If the answer the player provided was not right, the player is informed but nothing happens to the score.
    else:
        print("Sorry, you were wrong! The correct option was " + humantype + "!")

# Game informs player that their score will be displayed below and then does so.
print("Your score will be displayed below!")
print("Score : " + str(score))

# Game tells player if their score was good (more or equal to 3), bad (less than 3), or amazing (equal to 5).
if score == 5:
    print("You have the absolute best score! (5/5)")
elif score < 3:
    print("Your score was less than 3. Try better next time!")
elif score >= 3:
    print("Your score was quite good! (Over or equal to 3)")

# END OF CODE #
# STRATOS THIVAIOS - ©2023 #