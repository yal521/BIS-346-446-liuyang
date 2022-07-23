alphabet="abcdefghijklmnopqrstuvwxyz"
#2nd Part
character_counter = {}
def summarize_letters(string):
    string_lower = string.lower()
    for i in string_lower:
        if i in character_counter and i.isalpha():
            character_counter[i] = character_counter[i]+1
        if i not in character_counter and i.isalpha():
            character_counter[i]=1
    list_of_tuples = [(k,v) for k,v in character_counter.items()]
    return list_of_tuples
#3rd Part
#initializing a string of characters in alphabets
alphabets = 'You should find this exercise to be entertaining'
print(summarize_letters(alphabets))

#importing the string module
import string
#pulling all the alphabets
alphabet = set(string.ascii_lowercase)
#checking if our hardcoded string has all the alphabets
if set(alphabets.lower()) >= alphabet:
    print('The string ' +alphabets+' has all the letters in the alphabet ')
else:
    print('The string ' +alphabets+'does not contain all the letters in the alphabet')
