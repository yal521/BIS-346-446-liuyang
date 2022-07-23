import random
deck=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
value=0
card1 =random.choice(list(deck))
if card1 in ['Ace']:
    value1=11
elif card1 in ['Jack','Queen','King']:
    value1=10
elif card1 in ['2','3','4','5','6','7','8','9','10']:
    value1=int(card1)
    
    
card2 =random.choice(list(deck))
if card2 in ['Ace']:
    value2=11
elif card2 in ['Jack','Queen','King']:
    value2=10
elif card2 in ['2','3','4','5','6','7','8','9','10']:
    value2=int(card2)
    
    
print(card1)
print(card2)
print('Total value is', value1+value2)

