import random
deck=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
value1=0
value2=0
card1 =random.choice(list(deck))
if card1 in ['Ace']:
    value1=11
elif card1 in ['Jack','Queen','King']:
    value1=10
elif card1 in ['2','3','4','5','6','7','8','9','10']:
    value1=int(card1)
    
    
card2 =random.choice(list(deck))
if card2 in ['Ace'] and card2 != card1:
    value2=11
elif card2 in ['Jack','Queen','King'] and card2 != card1:
    value2=10
elif card2 in ['2','3','4','5','6','7','8','9','10'] and card2 != card1:
    value2=int(card2)

print(card1)
print(card2)
print('Total value is', value1+value2)

