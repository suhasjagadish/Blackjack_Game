import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand_card = random.choice(cards)
    return rand_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

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


user_card = []
dealer_card = []
is_game_over = False

for _ in range(2):
    user_card.append(deal_card())
    dealer_card.append(deal_card())


user_score = calculate_score(user_card)
dealer_score = calculate_score(dealer_card)

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


print(f"computer cards: {dealer_card}",)
print(f"compute score: {dealer_score}")
print(compare_scores(dealer_score, user_score))