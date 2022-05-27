# Blackjack Game made using Python

Blackjack is a popular card game played in most of the casino.This is an intuition to replicate the same card game using Python programme.
This code uses the command line for taking the inputs from the users to be interactive.

## Rules of Blackjack

Brief set of rules for readers who have never played Blackjack. The magic number for Blackjack is 21. The values for all the cards dealt to a player are added and if the sum exceeds 21, the player busts and loses instantly.If a player gets an exact 21, the player wins against the dealer. Otherwise, in order to win, the sum of the player’s cards must be more than the sum of the dealer’s cards. Each face card has a definite value of 10, whereas the ace can be counted as 1 or 11 suitable to the player’s chances of winning. The value of the rest of the cards is defined by their number.

## Module Used

Modules in Python can have some classes, functions and variables.

- In this **Python Project** I have used **Random** module, so that the cards should dealt not be biased for Player and Dealer.
- In Random module **random.choice()** is used to select a card from the card deck.

## Concepts used

- Used the concepts of **Conditional statements** ('if' and 'else'), **Looping statements** ('for' and 'while')
- Used **Functions** to cut down the repetitive coding of the same conditions.

## Game Design

### Some Fundamental Values

Each game of cards requires fundamental values like the cards and the values for each card. In this game we give Ace a value of 1/11, King-Queen-Jack and Ten a value of 10 and rest of the cards take their respective value.

''' Python

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

'''

### Dealing card

With the help of 'random' module i have used 'random.choice()' to select a card for the deck I created earlier
and wrapped it up 'deal_card()' function to use it with out repeating the code for all the time.  

''' Python

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand_card = random.choice(cards)
    return rand_card

'''
With the use of 'for' and 'range' 2 cards are dealt to the user and the dealer and is stored in list 'users_card' and 'dealer_card'

''' Python

user_card = []
dealer_card = []
is_game_over = False

for _ in range(2):
    user_card.append(deal_card())
    dealer_card.append(deal_card())

'''

### Calculate and Compare of scores

To calculate the scores of the card dealt a function is created to know the results

''' Python

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

'''

To Compare the scores obtained for the dealer and user, the results are returned as the Blackjack rules

''' python

user_score = calculate_score(user_card)
dealer_score = calculate_score(dealer_card)

'''

''' Python

def compare_scores(dealercards, usercards):
    if user_score == 0:
        return "You win with a blackjack"
    elif dealer_score == 0:
        return "Dealer has a Blackjack "
    elif user_score == dealer_score :
        return "PUSH"
    elif user_score > 21:
        return "YOU burst,Dealer win "
    elif dealer_score > 21:
        return "Dealer burst,you win"
    elif user_score > dealer_score :
        return "You win"
    else:
        return "Dealer win"

'''

### The Game

I have used a while loop for running the game since we do not know when the user will stand. I have defined 'is_game_over' as a flag to keep the check for the termination of the loop

''' Python

while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(dealer_card)
    print(f"Your cards are {user_card} and score is {user_score}")
    print(f"Dealer's first card: {dealer_card[0]} ")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        if user_score == 21 :
            is_game_over = True
        hit = input("Type 'Y' to hit and 'N' to stand\n").upper()
        if hit == "Y":
            user_card.append(deal_card())
        elif hit == "N":
            is_game_over = True
        else:
            is_game_over = True

while dealer_score != 0 and dealer_score < 17:
    dealer_card.append(deal_card())
    dealer_score = calculate_score(dealer_card)

'''

### The result

The winner of the game is showed after comparing the scores of all the cards dealt to the Dealer and User
''' Python

print(f"computer cards: {dealer_card}",)
print(f"compute score: {dealer_score}")
print(compare_scores(dealer_score, user_score))

'''
