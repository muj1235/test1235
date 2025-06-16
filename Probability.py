import random

# we want to estimate and understand the chance of getting 21 on the first draw (blackjack)

# define card values
king = 10
queen = 10
jack = 10
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
ten = 10
ace = "ace"  # will handle as 11 or 1

# full deck (each card appears 4 times)
Event = [
    ace, ace, ace, ace,
    king, king, king, king,
    queen, queen, queen, queen,
    jack, jack, jack, jack,
    ten, ten, ten, ten,
    two, two, two, two,
    three, three, three, three,
    four, four, four, four,
    five, five, five, five,
    six, six, six, six,
    seven, seven, seven, seven,
    eight, eight, eight, eight,
    nine, nine, nine, nine
]

# draw two cards randomly
A = random.choice(Event)
B = random.choice(Event)

# function to convert card to value
def card_value(card, current_total):
    if card == "ace":
        return 11 if current_total + 11 <= 21 else 1
    elif card in ["jack", "queen", "king"]:
        return 10
    return card

# calculate total hand value
myhand = 0
myhand += card_value(A, myhand)
myhand += card_value(B, myhand)

# print results
print("First card:", A)
print("Second card:", B)
print("Total hand:", myhand)

# compute exact theoretical probability of getting blackjack
prob_blackjack = (4/52)*(16/51) + (16/52)*(4/51)
print("The probability of getting 21 on the first draw is:", (4/52)*(16/51) + (16/52)*(4/51), " because casinos want the adavantage this is why you should stop gambling.")